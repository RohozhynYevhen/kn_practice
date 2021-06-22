import tkinter as tk
from mpmath import *

mp.dps = 25; mp.pretty = True

# Функция добавления чисел 
def add_digit(digit):
    calc['state'] = tk.NORMAL
    value = calc.get()
    if value[0] == '0' and len(value) == 1:
        value = value[1:]
        value += str(digit)
    elif value == 'error':
        value = str(digit)
    else:
        value += str(digit) 
    calc.delete(0,tk.END)
    calc.insert(0, value)
    calc['state'] = tk.DISABLED
    
# Функция добавления знаков операции
def add_operation(operation):
    calc['state'] = tk.NORMAL
    value = calc.get()
    if value[-1] in '+-/*^%':
        value = value[:-1]
    calc.delete(0, tk.END)
    calc.insert(0, value + operation)
    calc['state'] = tk.DISABLED

# Функция подсчета
def calculate():
    calc['state'] = tk.NORMAL
    value = calc.get()
    if value[-1] in '+-/*^%':
        value = value + value[:-1]
    value = value.replace('^', '**')
    calc.delete(0, tk.END)
    try:
        calc.insert(0, eval(value))
    except (NameError, SyntaxError):
        calc.insert(0, 'error')
    except ZeroDivisionError:
        calc.insert(0, 'error')
    calc['state'] = tk.DISABLED

# Функция очистки всей строки
def clear_all():
    calc['state'] = tk.NORMAL
    calc.delete(0, tk.END)
    calc.insert(0, '0')
    calc['state'] = tk.DISABLED

# Функция очистки по одному символу
def clear():
    calc['state'] = tk.NORMAL
    value = calc.get()
    if len(value) == 1:
        value = '0'
    elif value == 'error':
        value = '0'
    else:
        value = value[:-1]
    calc.delete(0, tk.END)
    calc.insert(0, value)
    calc['state'] = tk.DISABLED

# Функция перевода с 10с в 2с 
def binary():
    calc['state'] = tk.NORMAL
    value = calc.get()
    if value == 'error':
        value = 'error'
    else:
        if value.find('.') == -1:
            value = bin(int(value))
            value = value[2:]
        else:
            value = 'error'
    calc.delete(0, tk.END)
    calc.insert(0, value)
    calc['state'] = tk.DISABLED

# Функция перевода с 2с в 10с 
def dec():
    calc['state'] = tk.NORMAL
    value = calc.get()
    if value == 'error':
        value = 'error'
    else:
        try:
            value = str(int(value, 2))
        except ValueError:
            value = str(value)
    calc.delete(0, tk.END)
    calc.insert(0, value)
    calc['state'] = tk.DISABLED

# Создание окна    
win = tk.Tk()
win.wm_attributes('-alpha', 0.95)
win.geometry(f"420x310+100+200")
win['bg'] = '#FFFFFF'
win.resizable(width=False, height=False) 
win.title('Калькуляр')

# Поле для ввода
calc = tk.Entry(win, justify = tk.RIGHT, font=('Arial', 15), width = 15, bd = 2)
calc.insert(0, '0')
calc['state'] = tk.DISABLED
calc.config(background="white", disabledbackground="white")
calc.grid(row = 0, column = 0, columnspan=7, stick='we', padx = 2)

# Кнопки 1 ряд
b1 = tk.Button(text='Bin', bd = 1, font=('Arial', 13), command = binary).grid(row=1, column=0, stick='we', padx = 2, pady = 2)
b2 = tk.Button(text='Dec', bd = 1, font=('Arial', 13), command = dec).grid(row=1, column=1, stick='we', padx = 2, pady = 2)
b3 = tk.Button(text='<', bd = 1, font=('Arial', 13), command=lambda : clear()).grid(row=1, column=5, stick='we', padx = 2, pady = 2)
b4 = tk.Button(text='C', bd = 1, font=('Arial', 13), command=lambda : clear_all()).grid(row=1, column=6, stick='wens', padx = 2, pady = 2)

# Кнопки 2 ряд
tk.Button(text='1', bd = 1, font=('Arial', 13), command=lambda : add_digit(1)).grid(row=2, column=0, stick='wens', padx = 2, pady = 2)
tk.Button(text='2', bd = 1, font=('Arial', 13), command=lambda : add_digit(2)).grid(row=2, column=1, stick='wens', padx = 2, pady = 2)
tk.Button(text='3', bd = 1, font=('Arial', 13), command=lambda : add_digit(3)).grid(row=2, column=2, stick='wens', padx = 2, pady = 2)
tk.Button(text='+', bd = 1, font=('Arial', 13), command=lambda : add_operation('+')).grid(row=2, column=6, stick='wens', padx = 2, pady = 2)
tk.Button(text='cos', bd = 1, font=('Arial', 13), command=lambda : add_digit('cos(')).grid(row=2, column=3, stick='wens', padx = 2, pady = 2)
tk.Button(text='sin', bd = 1, font=('Arial', 13), command=lambda : add_digit('sin(')).grid(row=2, column=4, stick='wens', padx = 2, pady = 2)
tk.Button(text='tan', bd = 1, font=('Arial', 13), command=lambda : add_digit('tan(')).grid(row=2, column=5, stick='wens', padx = 2, pady = 2)

# Кнопки 3 ряд
tk.Button(text='4', bd = 1, font=('Arial', 13), command=lambda : add_digit(4)).grid(row=3, column=0, stick='wens', padx = 2, pady = 2)
tk.Button(text='5', bd = 1, font=('Arial', 13), command=lambda : add_digit(5)).grid(row=3, column=1, stick='wens', padx = 2, pady = 2)
tk.Button(text='6', bd = 1, font=('Arial', 13), command=lambda : add_digit(6)).grid(row=3, column=2, stick='wens', padx = 2, pady = 2)
tk.Button(text='-', bd = 1, font=('Arial', 13), command=lambda : add_operation('-')).grid(row=3, column=6, stick='wens', padx = 2, pady = 2)
tk.Button(text='(', bd = 1, font=('Arial', 13), command=lambda : add_digit('(')).grid(row=3, column=5, stick='wens', padx = 2, pady = 2)
tk.Button(text='cot', bd = 1, font=('Arial', 13), command=lambda : add_digit('cot(')).grid(row=3, column=3, stick='wens', padx = 2, pady = 2)
tk.Button(text='^x', bd = 1, font=('Arial', 13), command=lambda : add_operation('^')).grid(row=3, column=4, stick='wens', padx = 2, pady = 2)

# Кнопки 4 ряд
tk.Button(text='7', bd = 1, font=('Arial', 13), command=lambda : add_digit(7)).grid(row=4, column=0, stick='wens', padx = 2, pady = 2)
tk.Button(text='8', bd = 1, font=('Arial', 13), command=lambda : add_digit(8)).grid(row=4, column=1, stick='wens', padx = 2, pady = 2)
tk.Button(text='9', bd = 1, font=('Arial', 13), command=lambda : add_digit(9)).grid(row=4, column=2, stick='wens', padx = 2, pady = 2)
tk.Button(text='/', bd = 1, font=('Arial', 13), command=lambda : add_operation('/')).grid(row=4, column=6, stick='wens', padx = 2, pady = 2)
tk.Button(text=')', bd = 1, font=('Arial', 13), command=lambda : add_digit(')')).grid(row=4, column=5, stick='wens', padx = 2, pady = 2)
tk.Button(text='√', bd = 1, font=('Arial', 13), command=lambda : add_digit('sqrt(')).grid(row=4, column=3, stick='wens', padx = 2, pady = 2)
tk.Button(text='pi', bd = 1, font=('Arial', 13), command=lambda : add_digit('pi')).grid(row=4, column=4, stick='wens', padx = 2, pady = 2)

# Кнопки 5 ряд
tk.Button(text='0', bd = 1, font=('Arial', 13), command=lambda : add_digit(0)).grid(row=5, column=0, stick='wens', padx = 2, pady = 2)
tk.Button(text='*', bd = 1, font=('Arial', 13), command=lambda : add_operation('*')).grid(row=5, column=6, stick='wens', padx = 2, pady = 2)
tk.Button(text='=', bd = 1, font=('Arial', 13), command=lambda : calculate()).grid(row=5, column=5, stick='wens', padx = 2, pady = 2)
tk.Button(text='.', bd = 1, font=('Arial', 13), command=lambda : add_operation('.')).grid(row=5, column=1, stick='wens', padx = 2, pady = 2)
tk.Button(text='log', bd = 1, font=('Arial', 13), command=lambda : add_digit('log(')).grid(row=5, column=3, stick='wens', padx = 2, pady = 2)
tk.Button(text='ln', bd = 1, font=('Arial', 13), command=lambda : add_digit('ln(')).grid(row=5, column=4, stick='wens', padx = 2, pady = 2)
tk.Button(text='%', bd = 1, font=('Arial', 13), command=lambda : add_operation('%')).grid(row=5, column=2, stick='wens', padx = 2, pady = 2)

# Устанавка высоты для кнопок
win.grid_columnconfigure(0, minsize=60)
win.grid_columnconfigure(1, minsize=60)
win.grid_columnconfigure(2, minsize=60)
win.grid_columnconfigure(3, minsize=60)
win.grid_columnconfigure(4, minsize=60)
win.grid_columnconfigure(5, minsize=60)
win.grid_columnconfigure(6, minsize=60)
win.grid_columnconfigure(7, minsize=60)

# Установка ширины для кнопок
win.grid_rowconfigure(1, minsize=30)
win.grid_rowconfigure(2, minsize=60)
win.grid_rowconfigure(3, minsize=60)
win.grid_rowconfigure(4, minsize=60)
win.grid_rowconfigure(5, minsize=60)

win.mainloop()
