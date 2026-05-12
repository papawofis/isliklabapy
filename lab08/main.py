```python
import tkinter as tk
from tkinter import messagebox
import random

# ========== ИСКЛЮЧЕНИЯ ==========
class BError(Exception): pass
class GameOver(BError): pass

# ========== КОРАБЛЬ ==========
class Ship:
    def __init__(self, cells):
        self.__cells = set(cells)      # name mangling -> _Ship__cells
        self.__hits = set()            # name mangling -> _Ship__hits
    
    def hit(self, xy):
        self.__hits.add(xy)
        return self.__hits >= self.__cells
    
    def is_destroyed(self):
        return self.__hits >= self.__cells
    
    def has_hit(self, xy):
        return xy in self.__hits
    
    def get_hits_count(self):
        return len(self.__hits)
    
    def get_cells_count(self):
        return len(self.__cells)


# ========== ДОСКА ==========
class Board:
    def __init__(self):
        self.__cells = {}          # name mangling -> _Board__cells
        self.__fired = set()       # name mangling -> _Board__fired
        self.__ships = []          # name mangling -> _Board__ships
    
    def place(self, cells):
        # Проверка зоны вокруг
        z = {(x+dx, y+dy) for (x, y) in cells for dx in (-1,0,1) for dy in (-1,0,1)}
        if all(0 <= x < 10 and 0 <= y < 10 and (x, y) not in self.__cells for x, y in z):
            ship = Ship(cells)
            ship.__cells =0
            for cell in cells:
                self.__cells[cell] = ship
            self.__ships.append(ship)
            return True
        return False
    
    def shoot(self, xy):
        if xy in self.__fired:
            return None
        self.__fired.add(xy)
        
        if xy in self.__cells:
            ship = self.__cells[xy]
            is_destroyed = ship.hit(xy)
            return 'd' if is_destroyed else 'h'
        return 'm'
    
    def alive(self):
        return any(not ship.is_destroyed() for ship in self.__ships)
    
    def is_fired(self, xy):
        """Был ли выстрел по клетке?"""
        return xy in self.__fired
    
    def has_ship(self, xy):
        """Есть ли корабль в клетке?"""
        return xy in self.__cells
    
    def get_ship(self, xy):
        """Получить корабль по клетке"""
        return self.__cells.get(xy, None)
    
    def get_ship_state(self, xy):
        """Получить состояние клетки для отрисовки"""
        if xy in self.__fired:
            if xy in self.__cells:
                ship = self.__cells[xy]
                if ship.is_destroyed():
                    return 'destroyed'      # подбит целиком
                return 'wounded'            # ранен
            return 'miss'                   # мимо
        return 'water'                      # вода

# ========== ИГРА ==========
class Game:
    def __init__(self):
        self.__boards = [Board(), Board()]   # name mangling -> _Game__boards
        self.__turn = 0                      # 0 - игрок, 1 - компьютер
        self.__over = False                  # флаг окончания игры
        
        # Расстановка кораблей
        for board in self.__boards:
            for size in [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]:
                placed = False
                for _ in range(99):
                    x, y = random.randint(0, 9), random.randint(0, 9)
                    dx, dy = random.choice([(1, 0), (0, 1)])
                    cells = [(x + dx*i, y + dy*i) for i in range(size)]
                    
                    # Проверка границ
                    if all(0 <= cx < 10 and 0 <= cy < 10 for cx, cy in cells):
                        if board.place(cells):
                            placed = True
                            break
                if not placed:
                    # Запасной вариант - вручную ставим
                    for _ in range(100):
                        x, y = random.randint(0, 9), random.randint(0, 9)
                        cells = [(x, y)]
                        if board.place(cells):
                            break
    
    def shoot(self, xy):
        """Выстрел игрока"""
        if self.__over:
            raise GameOver
        if self.__turn != 0:
            return None
        
        result = self.__boards[1].shoot(xy)
        
        if result == 'm':
            self.__turn = 1
        if result is not None and not self.__boards[1].alive():
            self.__over = True
            raise GameOver
        
        return result
    
    def ai_shoot(self):
        """Выстрел компьютера"""
        if self.__over:
            raise GameOver
        if self.__turn != 1:
            return None, None
        
        # Простой AI - случайный выстрел
        free = [(x, y) for x in range(10) for y in range(10) 
                if not self.__boards[0].is_fired((x, y))]
        
        if not free:
            self.__over = True
            raise GameOver
        
        xy = random.choice(free)
        result = self.__boards[0].shoot(xy)
        
        if result == 'm':
            self.__turn = 0
        if not self.__boards[0].alive():
            self.__over = True
            raise GameOver
        
        return xy, result
    
    # ===== Геттеры для GUI =====
    def get_board(self, index):
        """Получить доску (только для чтения через геттеры)"""
        return self.__boards[index]
    
    def is_player_turn(self):
        """Чей ход? True - игрок, False - компьютер"""
        return self.__turn == 0
    
    def is_game_over(self):
        return self.__over
    
    def get_winner(self):
        """Определить победителя"""
        if self.__over:
            if not self.__boards[1].alive():
                return "Ты"
            if not self.__boards[0].alive():
                return "Комп"
        return None

# ========== GUI ==========
SZ = 35
CLR = {
    'water': 'steelblue',
    'ship': 'gray',
    'wounded': 'orange',
    'destroyed': 'red',
    'miss': 'white'
}

class App:
    def __init__(self, root):
        self.__root = root
        root.title("Морской бой")
        root.resizable(False, False)
        
        # Canvas для досок
        self.__canvas = [
            tk.Canvas(root, width=SZ*10+2, height=SZ*10+2),
            tk.Canvas(root, width=SZ*10+2, height=SZ*10+2)
        ]
        
        self.__label = tk.Label(root, font="Arial 12 bold")
        self.__label.pack()
        
        for canvas in self.__canvas:
            canvas.pack(side=tk.LEFT, padx=10)
        
        tk.Button(root, text="Заново", command=self.__new_game).pack()
        
        self.__canvas[1].bind("<Button-1>", self.__click)
        self.__game = None
        self.__new_game()
    
    def __new_game(self):
        """Начать новую игру"""
        self.__game = Game()
        self.__draw()
        self.__label.config(text="Твой ход!")
    
    def __draw(self):
        """Отрисовка обоих полей"""
        for idx, canvas in enumerate(self.__canvas):
            canvas.delete("all")
            board = self.__game.get_board(idx)
            hide_ships = (idx == 1)  # на доске компьютера прячем корабли
            
            for y in range(10):
                for x in range(10):
                    color = self.__get_cell_color(board, x, y, hide_ships)
                    canvas.create_rectangle(
                        x*SZ, y*SZ, x*SZ+SZ, y*SZ+SZ,
                        fill=color, outline='black'
                    )
    
    def __get_cell_color(self, board, x, y, hide_ships):
        """Определить цвет клетки (используя геттеры)"""
        xy = (x, y)
        
        # Были ли выстрел?
        if board.is_fired(xy):
            if board.has_ship(xy):
                ship = board.get_ship(xy)
                if ship.is_destroyed():
                    return CLR['destroyed']
                return CLR['wounded']
            return CLR['miss']
        
        # Корабль виден только на своей доске
        if board.has_ship(xy) and not hide_ships:
            return CLR['ship']
        
        return CLR['water']
    
    def __click(self, event):
        """Обработка клика игрока"""
        # Проверка - чей ход
        if not self.__game.is_player_turn():
            return
        
        xy = (event.x // SZ, event.y // SZ)
        
        try:
            result = self.__game.shoot(xy)
            self.__draw()
            
            if result == 'm':
                self.__label.config(text="Комп думает...")
                self.__root.after(700, self.__ai_move)
            else:
                self.__label.config(text="Твой ход!" if result != 'm' else "Комп думает...")
                
            self.__check_game_over()
            
        except GameOver:
            self.__end_game()
    
    def __ai_move(self):
        """Ход компьютера"""
        try:
            xy, result = self.__game.ai_shoot()
            self.__draw()
            
            if result == 'm':
                self.__label.config(text="Твой ход!")
            else:
                self.__label.config(text="Комп ещё...")
                self.__root.after(600, self.__ai_move)
            
            self.__check_game_over()
            
        except GameOver:
            self.__end_game()
    
    def __check_game_over(self):
        """Проверка окончания игры"""
        if self.__game.is_game_over():
            self.__end_game()
    
    def __end_game(self):
        """Завершение игры"""
        winner = self.__game.get_winner()
        self.__label.config(text=f"Победил {winner}!")
        messagebox.showinfo("Конец игры", f"Победил {winner}!")

if __name__ == "__main__":
    App(tk.Tk())
    tk.mainloop()
```
