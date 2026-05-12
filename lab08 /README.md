ЗАДАНИЕЛабы.py
--------
#### Задание:Реализуйте приложение с GUI (приложения-игры допускается делать с использованием TUI-пакетов) по своему варианту. Можно изменить задание на собственную тему, согласовав с преподавателем. Требования:

    - приложение должно быть написано с применением ОО парадигмы
    - исключительные ситуации должны обрабатываться с использованием собственных исключений
    - GUI/TUI фреймворки не должны повторяться в группе
# Морской бой (Sea Battle)


### Цветовая индикация:
- **Синий** - вода (не стреляли)
- **Белый** - промах
- **Оранжевый** - раненый корабль
- **Красный** - уничтоженный корабль
- **Серый** - ваш корабль (виден только на левой доске)
- **Скрыты** - корабли компьютера (не видны до попадания)

  
### Требования:
- Python 3.6 или выше
- Tkinter (обычно входит в стандартную установку Python)

### Установка и запуск:

1. **Сохраните код** в файл с расширением `.py`, например:
   ```bash
   sea_battle.py


### Ход работы :
```python
import tkinter as tk
from tkinter import messagebox
import random

# ========== ИСКЛЮЧЕНИЯ ==========
# Определяем собственные исключения для игры
class BError(Exception):      # Базовое исключение (пока не используется)
    pass

class GameOver(BError):       # Исключение для окончания игры
    pass


# ========== КОРАБЛЬ ==========
class Ship:
    """Класс, представляющий один корабль"""
    
    def __init__(self, cells):
        # cells - набор координат клеток, которые занимает корабль
        self.__cells = set(cells)      # Приватный атрибут: клетки корабля
        self.__hits = set()            # Приватный атрибут: попадания по кораблю
    
    def hit(self, xy):
        """Обрабатывает попадание по кораблю. Возвращает True, если корабль уничтожен"""
        self.__hits.add(xy)            # Добавляем координату попадания
        return self.__hits >= self.__cells  # Проверяем, все ли клетки подбиты
    
    def is_destroyed(self):
        """Проверяет, уничтожен ли корабль целиком"""
        return self.__hits >= self.__cells
    
    def has_hit(self, xy):
        """Проверяет, было ли попадание в данную клетку"""
        return xy in self.__hits
    
    def get_hits_count(self):
        """Возвращает количество попаданий по кораблю"""
        return len(self.__hits)
    
    def get_cells_count(self):
        """Возвращает общее количество клеток корабля"""
        return len(self.__cells)


# ========== ДОСКА ==========
class Board:
    """Класс, представляющий игровое поле (10x10)"""
    
    def __init__(self):
        self.__cells = {}          # Словарь: клетка -> корабль, который там находится
        self.__fired = set()       # Множество клеток, по которым уже стреляли
        self.__ships = []          # Список всех кораблей на доске
    
    def place(self, cells):
        """
        Размещает корабль на доске по заданным клеткам
        Возвращает True, если размещение удалось, False - если нет
        """
        # Создаем зону вокруг корабля (включая диагонали)
        z = {(x+dx, y+dy) for (x, y) in cells for dx in (-1,0,1) for dy in (-1,0,1)}
        
        # Проверяем, что все клетки зоны в пределах поля и свободны
        if all(0 <= x < 10 and 0 <= y < 10 and (x, y) not in self.__cells for x, y in z):
            ship = Ship(cells)           # Создаем новый корабль
            ship.__cells = 0             # ВНИМАНИЕ: здесь баг! (прямой доступ к приватному атрибуту)
            for cell in cells:           # Размещаем координаты на доске
                self.__cells[cell] = ship
            self.__ships.append(ship)    # Добавляем корабль в список
            return True
        return False
    
    def shoot(self, xy):
        """
        Обрабатывает выстрел по клетке
        Возвращает:
        'd' - если корабль уничтожен
        'h' - если попадание (ранен)
        'm' - если мимо
        None - если уже стреляли по этой клетке
        """
        if xy in self.__fired:           # Если уже стреляли сюда
            return None
        self.__fired.add(xy)             # Отмечаем, что стреляли
        
        if xy in self.__cells:           # Если в клетке есть корабль
            ship = self.__cells[xy]      # Получаем корабль
            is_destroyed = ship.hit(xy)  # Попадаем по кораблю
            return 'd' if is_destroyed else 'h'  # Уничтожен или ранен
        return 'm'                       # Мимо
    
    def alive(self):
        """Проверяет, есть ли на доске непотопленные корабли"""
        return any(not ship.is_destroyed() for ship in self.__ships)
    
    def is_fired(self, xy):
        """Был ли уже выстрел по этой клетке?"""
        return xy in self.__fired
    
    def has_ship(self, xy):
        """Есть ли корабль в данной клетке?"""
        return xy in self.__cells
    
    def get_ship(self, xy):
        """Возвращает корабль, находящийся в клетке (или None)"""
        return self.__cells.get(xy, None)
    
    def get_ship_state(self, xy):
        """Возвращает состояние клетки для отрисовки"""
        if xy in self.__fired:                     # Если стреляли
            if xy in self.__cells:                 # Если попали
                ship = self.__cells[xy]
                if ship.is_destroyed():
                    return 'destroyed'             # Корабль уничтожен
                return 'wounded'                   # Корабль ранен
            return 'miss'                          # Выстрел мимо
        return 'water'                             # Вода (не стреляли)


# ========== ИГРА ==========
class Game:
    """Основной класс игры, управляющий логикой"""
    
    def __init__(self):
        self.__boards = [Board(), Board()]   # Две доски: [0] - игрока, [1] - компьютера
        self.__turn = 0                      # Чей ход: 0 - игрок, 1 - компьютер
        self.__over = False                  # Флаг окончания игры
        
        # Расстановка кораблей на обеих досках
        for board in self.__boards:
            # Список размеров кораблей: 1 четырехпалубный, 2 трехпалубных и т.д.
            for size in [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]:
                placed = False
                # Пытаемся разместить корабль случайным образом (до 99 попыток)
                for _ in range(99):
                    x, y = random.randint(0, 9), random.randint(0, 9)
                    dx, dy = random.choice([(1, 0), (0, 1)])  # Горизонтально или вертикально
                    cells = [(x + dx*i, y + dy*i) for i in range(size)]
                    
                    # Проверяем, что все клетки в пределах поля
                    if all(0 <= cx < 10 and 0 <= cy < 10 for cx, cy in cells):
                        if board.place(cells):
                            placed = True
                            break
                
                # Если не удалось разместить за 99 попыток - ставим однопалубный
                if not placed:
                    for _ in range(100):
                        x, y = random.randint(0, 9), random.randint(0, 9)
                        cells = [(x, y)]
                        if board.place(cells):
                            break
    
    def shoot(self, xy):
        """
        Выстрел игрока по доске компьютера
        Возвращает результат выстрела ('m', 'h', 'd')
        """
        if self.__over:
            raise GameOver                 # Игра окончена
        if self.__turn != 0:
            return None                    # Не ход игрока
        
        result = self.__boards[1].shoot(xy)   # Стреляем по доске компьютера
        
        if result == 'm':                    # Если мимо - ход переходит компьютеру
            self.__turn = 1
        if result is not None and not self.__boards[1].alive():  # Если все корабли уничтожены
            self.__over = True
            raise GameOver
        
        return result
    
    def ai_shoot(self):
        """
        Выстрел компьютера по доске игрока
        Возвращает (координаты, результат) или (None, None) если не ход ИИ
        """
        if self.__over:
            raise GameOver
        if self.__turn != 1:
            return None, None              # Не ход компьютера
        
        # Простой ИИ: выбирает случайную клетку, в которую еще не стреляли
        free = [(x, y) for x in range(10) for y in range(10) 
                if not self.__boards[0].is_fired((x, y))]
        
        if not free:                        # Если нет свободных клеток
            self.__over = True
            raise GameOver
        
        xy = random.choice(free)            # Случайный выбор
        result = self.__boards[0].shoot(xy)  # Стреляем по доске игрока
        
        if result == 'm':                   # Если мимо - ход игроку
            self.__turn = 0
        if not self.__boards[0].alive():    # Если все корабли игрока уничтожены
            self.__over = True
            raise GameOver
        
        return xy, result
    
    # Геттеры для GUI
    def get_board(self, index):
        """Возвращает доску (0 - игрока, 1 - компьютера)"""
        return self.__boards[index]
    
    def is_player_turn(self):
        """Чей ход? True - игрок, False - компьютер"""
        return self.__turn == 0
    
    def is_game_over(self):
        """Проверяет, окончена ли игра"""
        return self.__over
    
    def get_winner(self):
        """Определяет победителя"""
        if self.__over:
            if not self.__boards[1].alive():
                return "Ты"                # Победил игрок
            if not self.__boards[0].alive():
                return "Комп"              # Победил компьютер
        return None


# ========== GUI (Графический интерфейс) ==========
SZ = 35                      # Размер одной клетки в пикселях
CLR = {                      # Цвета для различных состояний
    'water': 'steelblue',    # Вода (не стреляли)
    'ship': 'gray',          # Корабль (виден только на своей доске)
    'wounded': 'orange',     # Раненый корабль
    'destroyed': 'red',      # Уничтоженный корабль
    'miss': 'white'          # Промах
}

class App:
    """Главный класс приложения с графическим интерфейсом"""
    
    def __init__(self, root):
        self.__root = root
        root.title("Морской бой")
        root.resizable(False, False)          # Запрещаем изменение размера окна
        
        # Создаем два холста для отрисовки досок
        self.__canvas = [
            tk.Canvas(root, width=SZ*10+2, height=SZ*10+2),
            tk.Canvas(root, width=SZ*10+2, height=SZ*10+2)
        ]
        
        # Создаем текстовую метку для отображения статуса игры
        self.__label = tk.Label(root, font="Arial 12 bold")
        self.__label.pack()
        
        # Размещаем холсты на окне
        for canvas in self.__canvas:
            canvas.pack(side=tk.LEFT, padx=10)
        
        # Кнопка для перезапуска игры
        tk.Button(root, text="Заново", command=self.__new_game).pack()
        
        # Привязываем обработчик клика к доске компьютера
        self.__canvas[1].bind("<Button-1>", self.__click)
        
        self.__game = None
        self.__new_game()                      # Запускаем новую игру
    
    def __new_game(self):
        """Начинает новую игру"""
        self.__game = Game()                   # Создаем новый экземпляр игры
        self.__draw()                          # Отрисовываем доски
        self.__label.config(text="Твой ход!")  # Обновляем статус
    
    def __draw(self):
        """Отрисовывает обе игровые доски"""
        for idx, canvas in enumerate(self.__canvas):
            canvas.delete("all")               # Очищаем холст
            board = self.__game.get_board(idx)
            hide_ships = (idx == 1)            # На доске компьютера прячем корабли
            
            # Проходим по всем клеткам (10x10)
            for y in range(10):
                for x in range(10):
                    # Определяем цвет клетки
                    color = self.__get_cell_color(board, x, y, hide_ships)
                    # Рисуем прямоугольник-клетку
                    canvas.create_rectangle(
                        x*SZ, y*SZ, x*SZ+SZ, y*SZ+SZ,
                        fill=color, outline='black'
                    )
    
    def __get_cell_color(self, board, x, y, hide_ships):
        """Определяет цвет клетки в зависимости от ее состояния"""
        xy = (x, y)
        
        # Если по клетке уже стреляли
        if board.is_fired(xy):
            if board.has_ship(xy):            # Если в клетке был корабль
                ship = board.get_ship(xy)
                if ship.is_destroyed():
                    return CLR['destroyed']    # Уничтожен - красный
                return CLR['wounded']          # Ранен - оранжевый
            return CLR['miss']                 # Промах - белый
        
        # Если не стреляли и клетка занята кораблем
        if board.has_ship(xy) and not hide_ships:
            return CLR['ship']                 # Корабль - серый (виден только на своей доске)
        
        return CLR['water']                    # Вода - синий
    
    def __click(self, event):
        """Обрабатывает клик мыши по доске компьютера"""
        # Проверяем, что ход игрока
        if not self.__game.is_player_turn():
            return
        
        # Определяем координаты клетки по клику
        xy = (event.x // SZ, event.y // SZ)
        
        try:
            result = self.__game.shoot(xy)      # Производим выстрел
            self.__draw()                       # Перерисовываем доски
            
            if result == 'm':                   # Если промах
                self.__label.config(text="Комп думает...")
                self.__root.after(700, self.__ai_move)  # Ход компьютера через 0.7 сек
            else:                               # Если попал
                self.__label.config(text="Твой ход!")
                
            self.__check_game_over()            # Проверяем, не окончена ли игра
            
        except GameOver:
            self.__end_game()                   # Завершаем игру
    
    def __ai_move(self):
        """Ход компьютера"""
        try:
            xy, result = self.__game.ai_shoot()  # Компьютер стреляет
            self.__draw()                        # Перерисовываем доски
            
            if result == 'm':                    # Если промах
                self.__label.config(text="Твой ход!")
            else:                                # Если попал
                self.__label.config(text="Комп ещё...")
                self.__root.after(600, self.__ai_move)  # Компьютер ходит снова
            
            self.__check_game_over()             # Проверяем, не окончена ли игра
            
        except GameOver:
            self.__end_game()                    # Завершаем игру
    
    def __check_game_over(self):
        """Проверяет, не окончена ли игра"""
        if self.__game.is_game_over():
            self.__end_game()
    
    def __end_game(self):
        """Завершает игру и показывает победителя"""
        winner = self.__game.get_winner()
        self.__label.config(text=f"Победил {winner}!")
        messagebox.showinfo("Конец игры", f"Победил {winner}!")


# ========== ТОЧКА ВХОДА ==========
if __name__ == "__main__":
    App(tk.Tk())          # Создаем окно и приложение
    tk.mainloop()         # Запускаем главный цикл обработки событий
```


##### Результат:
<img width="827" height="368" alt="image" src="https://github.com/user-attachments/assets/2fa54265-8237-4712-854b-db8cfa584ef1" />



##### Используемые материалы:

[Пакеты в Python](https://yandex.ru/video/preview/6795768651042013197?from=tabbar&parent-reqid=1777280500309801-18023372361586210236-balancer-l7leveler-kubr-yp-vla-11-BAL&text=пакеты+в+питоне)

[Модуль Tkinker в Python](https://yandex.ru/video/preview/7556322058098179161?from=tabbar&parent-reqid=1777280528378776-1632421795017964669-balancer-l7leveler-kubr-yp-vla-11-BAL&reqid=1777280500309801-18023372361586210236-balancerl7leveler-kubr-yp-vla-11-BAL&suggest_reqid=252038585173062242105017665169894&text=ткинтер+фреймворк)

[Наследственность в Python](https://www.google.com/url?esrc=s&q=&rct=j&sa=U&url=https://www.youtube.com/watch%3Fv%3D4ehsnUQ0P2A&ved=2ahUKEwjH8cz1_LKUAxVbORAIHU53A0YQtwJ6BAgHEAE&usg=AOvVaw13KQS7XgI33heXzM-9zY2P)

[Инкапсуляция в Python](https://www.google.com/url?esrc=s&q=&rct=j&sa=U&url=https://www.youtube.com/watch%3Fv%3DQX5ShMsI9RU&ved=2ahUKEwiw8pOl_bKUAxVmIBAIHbCPCg0QtwJ6BAgJEAE&usg=AOvVaw3P8SshscuTYoBB-EohCbkk)
