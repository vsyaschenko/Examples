import tkinter as tk
from tkinter import ttk
import sqlite3 

class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.db = db
        self.view_records()

    def init_main(self):
        # инициализация окна, добавление элементов
        # 
        # создаем командную панель (фрейм)
        # 1 цвет фона, 2 отступ 
        toolbar = tk.Frame(bg='#DDD', bd=2)
        # упаковываем панель. 1 прижать к верхнему краю, 2 растянуть по горизон.
        toolbar.pack(side=tk.TOP, fill=tk.X)
        
        # создаем кнопку
        # инициализируем картинку
        self.add_img = tk.PhotoImage(file='add.gif')
        # 1 принадлежность форме, 2 команда, 3 цвет фона, 4 отступ, 5 ???
        # 6 иконка        
        btn_open_dialog = tk.Button(toolbar, 
                                    text='Добавить позицию', 
                                    command=self.open_dialog, 
                                    bg='#DDD', 
                                    bd=0, 
                                    compound=tk.TOP, 
                                    image=self.add_img)
        # упаковываем кнопку с вырвавниванием по левому краю
        btn_open_dialog.pack(side=tk.LEFT) 
        
        self.update_img = tk.PhotoImage(file='add.gif')
        btn_edit_dialog = tk.Button(toolbar, 
                                    text='Редактировать',
                                    command=self.open_update_dialog,
                                    bg='#DDD',
                                    bd=0,
                                    compound=tk.TOP,
                                    image=self.update_img)
        btn_edit_dialog.pack(side=tk.LEFT)

        
        # добавляем таблицу
        columns = ('id', 'description', 'cost', 'total')
        self.tree = ttk.Treeview(self, 
                                    column=columns, 
                                    height=15, 
                                    show='headings')
        # инициализация колонок
        self.tree.column('id', width=30, anchor=tk.CENTER)
        self.tree.column('description', width=365, anchor=tk.CENTER)
        self.tree.column('cost', width=150, anchor=tk.CENTER)
        self.tree.column('total', width=100, anchor=tk.CENTER)
        # задаем заголовки
        self.tree.heading('id', text='id')
        self.tree.heading('description', text='Наименование')
        self.tree.heading('cost', text='Статья дохода/расхода')
        self.tree.heading('total', text='Сумма')

        self.tree.pack()

    def records(self, description, costs, total):
        self.db.insert_data(description, costs, total)
        self.view_records()

    def update_record(self, description, costs, total):
        self.db.c.execute('''
        UPDATE finance
        SET description=?, costs=?, total=?
        WHERE id=?''',
        (description, costs, total, self.tree.set(self.tree.selection()[0], 
                                                                    '#1')))
        self.db.conn.commit()
        self.view_records()

    def view_records(self):
        self.db.c.execute('''SELECT * 
                             FROM finance''')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def open_update_dialog(self):
        Update()

    def open_dialog(self):
        Child() 

# класс дочернего окна
class Child(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child()
        self.view = app
    
    def init_child(self):
        # инициализация окна, добавление элементов
        # 
        self.title('Добавить доходы\расходы')
        self.geometry('400x220+400+300')
        self.resizable(False, False)

        # устанавливаем надпись
        label_description = ttk.Label(self, text='Наименование')
        label_description.place(x=50, y=50)
        # добавляем поле ввода
        self.enty_description = ttk.Entry(self)
        self.enty_description.place(x=200,y=50)
        # надпись
        label_select = ttk.Label(self, text='Статья дохода/расхода')
        label_select.place(x=50, y=80)
        # выпадающий список
        self.combobox= ttk.Combobox(self, values=[u'Доход', u'Расход'])
        self.combobox.current(0) # значение по умолчанию
        self.combobox.place(x=200,y=80)
        # надпись   
        label_sum = ttk.Label(self, text='Сумма')
        label_sum.place(x=50, y=110)
        # полу ввода
        self.enty_money= ttk.Entry(self)
        self.enty_money.place(x=200,y=110)

        btn_cansel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cansel.place(x=300, y=170)

        self.btn_ok = ttk.Button(self, text='Добавить')
        self.btn_ok.place(x=220, y=170)
        self.btn_ok.bind('<Button-1>', 
                    lambda event: self.view.records(self.enty_description.get(),
                                                    self.combobox.get(),
                                                    self.enty_money.get()))

        # делаем окно модальным 
        self.grab_set()
        # удерживает фокус на окне, что бы окно было поверх основного
        self.focus_set()

class Update(Child):
    def __init__(self):
        super().__init__()
        self.init_edit()
        self.view = app
    
    def init_edit(self):
        self.title('Редактировать позиции')
        btn_edit = ttk.Button(self, text='Редактировать')
        btn_edit.place(x=205, y=170)
        btn_edit.bind('<Button-1>', 
        lambda event: self.view.update_record(self.enty_description.get(),
                                                self.combobox.get(),
                                                self.enty_money.get()))
        self.btn_ok.destroy()

class DB:
    def __init__(self):
        # устанавилваем соединение с базой данных. При отсутствии файла
        # база данных с таким именем будет создана
        self.conn = sqlite3.connect('finance.db')
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXISTS finance
                        (id integer primary key,
                        description text,
                        costs text,
                        total real)''')
        self.conn.commit()
        
    def insert_data(self, description, costs, total):
        self.c.execute('''INSERT INTO finance
                        (description, costs, total)
                        VALUES
                        (?, ?, ?)''', 
                        (description, costs, total))
        self.conn.commit()

if __name__ == '__main__': 
# код будет выполняться, если модуль исполняется в качестве основной программы
# это нужно для того, что бы данный код не исполнялся при импортировании модуля
    root = tk.Tk()
    db = DB()
    app = Main(root)
    app.pack() 
    root.title('Household finance')
    root.geometry('650x450+300+200') # размер окна + положение окна
    root.resizable(False, False)
    root.mainloop() # показать окно приложения