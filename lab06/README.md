ЗАДАНИЕЛабы.py
--------
#### Задание: Основная программа должна предоставлять:
графический пользовательский интерфейс с возможностями ввода требуемых параметров и отображения результатов расчёта,
возможность сохранить результаты в отчёт формата .doc или .xls (например, пакеты python-docx и openpyxl).


Элементарные частицы

Электрон
Нейтрон
Протон
Расчёт удельного заряда, комптоновской длины волны.
```python
import tkinter as tk
from tkinter import ttk, messagebox
from paket import particles, specific_charge, compton_wavelength
from paket.db_postgres import save_result, get_all_results
import docx
from datetime import datetime

class ParticleApp:
    def __init__(self, root):
        # Инициализация главного окна
        self.root = root
        self.root.title("Расчёт частиц")  # Заголовок окна
        self.root.geometry("700x550")    # Размер окна
        self.last_particle = self.last_spec = self.last_comp = ""  # Переменные для хранения последнего расчёта
        
        # Выпадающий список для выбора частицы
        self.combo = ttk.Combobox(root, values=list(particles.keys()), state="readonly", width=30)
        self.combo.pack(pady=5)
        self.combo.set("Выберите частицу")  # Текст по умолчанию
        
        # Кнопка расчёта
        self.btn_calc = tk.Button(root, text="Рассчитать", command=self.calculate, bg="lightyellow")
        self.btn_calc.pack(pady=5)
        
        # Поле для вывода результата
        self.result_var = tk.StringVar(value="Нажмите 'Рассчитать'")
        self.result_label = tk.Label(root, textvariable=self.result_var, font=("Arial", 10), justify="left")
        self.result_label.pack(pady=10)
        
        # Рамка для кнопок сохранения
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=5)
        # Кнопка сохранения в БД
        tk.Button(btn_frame, text="Сохранить в БД", command=self.save_to_db, bg="lightblue", width=18).pack(side="left", padx=5)
        # Кнопка сохранения в Word
        tk.Button(btn_frame, text="Сохранить в .docx", command=self.save_doc, bg="lightgreen", width=18).pack(side="left", padx=5)
        
        # Таблица для отображения истории расчётов
        self.tree = ttk.Treeview(root, columns=("id", "particle", "specific", "compton"), show="headings", height=6)
        # Настройка колонок таблицы
        for col, width in [("id", 40), ("particle", 100), ("specific", 180), ("compton", 180)]:
            self.tree.heading(col, text=col.capitalize())
            self.tree.column(col, width=width)
        self.tree.pack(pady=10, fill="both", expand=True)
        
        # Кнопка обновления истории
        tk.Button(root, text="Обновить историю", command=self.load_history, bg="lightgray").pack(pady=5)
        self.load_history()  # Загрузка истории при запуске
    
    def calculate(self):
        # Получение выбранной частицы
        particle = self.combo.get()
        # Проверка, что частица выбрана
        if particle == "Выберите частицу":
            messagebox.showwarning("Внимание", "Выберите частицу!")
            return
        
        # Получение массы и заряда частицы из словаря
        m, q = particles[particle]["mass"], particles[particle]["charge"]
        # Расчёт удельного заряда и комптоновской длины волны
        spec, comp = specific_charge(q, m), compton_wavelength(m)
        
        # Сохранение результатов последнего расчёта
        self.last_particle, self.last_spec, self.last_comp = particle, f"{spec:.2e}", f"{comp:.2e}"
        
        # Вывод результата на экран
        self.result_var.set(f"{particle}\nУд. заряд: {spec:.2e} Кл/кг\nКомпт. λ: {comp:.2e} м")
        messagebox.showinfo("Успех", "Расчёт выполнен!")
    
    def save_to_db(self):
        # Проверка, был ли произведён расчёт
        if not self.last_particle:
            messagebox.showwarning("Внимание", "Сначала выполните расчёт!")
            return
        try:
            # Сохранение результата в базу данных
            save_result(self.last_particle, self.last_spec, self.last_comp)
            messagebox.showinfo("Успех", "Сохранено в PostgreSQL!")
            self.load_history()  # Обновление отображаемой истории
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))
    
    def save_doc(self):
        # Проверка, был ли произведён расчёт
        if not self.last_particle:
            messagebox.showwarning("Внимание", "Сначала выполните расчёт!")
            return
        # Создание Word-документа
        doc = docx.Document()
        doc.add_heading('Отчёт по частицам', 0)
        # Добавление информации о расчёте
        doc.add_paragraph(f"Дата: {datetime.now()}\nЧастица: {self.last_particle}\nУдельный заряд: {self.last_spec} Кл/кг\nКомптоновская λ: {self.last_comp} м")
        # Сохранение файла с временной меткой
        doc.save(f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.docx")
        messagebox.showinfo("Готово", "Сохранено в .docx")
    
    def load_history(self):
        # Очистка таблицы
        for item in self.tree.get_children():
            self.tree.delete(item)
        try:
            # Загрузка всех записей из БД
            for row in get_all_results():
                self.tree.insert("", "end", values=(row['id'], row['particle'], row['specific'], row['compton']))
        except:
            # Если БД недоступна, выводим сообщение
            self.tree.insert("", "end", values=("", "Нет данных", "", ""))

# Точка входа в программу
if __name__ == "__main__":
    root = tk.Tk()           # Создание главного окна (закомментировано)
    app = ParticleApp(root)  # Создание экземпляра приложения (закомментировано)
    root.mainloop()          # Запуск главного цикла обработки событий (закомментировано)
```

##### Результат:
<img width="901" height="731" alt="image" src="https://github.com/user-attachments/assets/826b0884-5d93-4449-89e0-b16efbd0273d" />


##### Используемые материалы:

[Пакеты в Python](https://yandex.ru/video/preview/6795768651042013197?from=tabbar&parent-reqid=1777280500309801-18023372361586210236-balancer-l7leveler-kubr-yp-vla-11-BAL&text=пакеты+в+питоне)

[Модуль string в Python](https://yandex.ru/video/preview/7556322058098179161?from=tabbar&parent-reqid=1777280528378776-1632421795017964669-balancer-l7leveler-kubr-yp-vla-11-BAL&reqid=1777280500309801-18023372361586210236-balancer-l7leveler-kubr-yp-vla-11-BAL&suggest_reqid=252038585173062242105017665169894&text=ткинтер+фреймворк)
