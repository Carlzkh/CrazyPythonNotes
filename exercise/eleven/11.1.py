"""
1. 使用 Tkinter 编写图形界面的计算器。
"""
import tkinter
from tkinter import ttk


win = tkinter.Tk()
win.title("数字计算器")
win.geometry("500x350+200+10")

task1 = tkinter.Variable()

entry = tkinter.Entry(relief='sunken', font=('Courier New', 24), width=100, textvariable=task1)
entry.pack(side='top', pady=10)
p = tkinter.Frame(win)
p.pack(side='top')

names = ('1', '2', '3', '+', '4', '5', '6', '-', '7', '8', '9', '*', '0', '.', '/')
global b


def select():
    a = b
    task1.trace_add()
    print(a)


def set_one():
    task1.set(task1.get() + '1')


def set_two():
    task1.set(task1.get() + '2')
    print(task1)


def set_three():
    task1.set(task1.get() + '3')
    print(task1)
    print(type(task1.get()))


def set_four():
    task1.set(task1.get() + '4')


def set_five():
    task1.set(task1.get() + '5')


def set_six():
    task1.set(task1.get() + '6')


def set_seven():
    task1.set(task1.get() + '7')


def set_eight():
    task1.set(task1.get() + '8')


def set_nine():
    task1.set(task1.get() + '9')


def set_ten():
    task1.set(task1.get() + '0')


def set_chu():
    task1.set(task1.get() + '/')


def set_jia():
    task1.set(task1.get() + '+')


def set_jian():
    task1.set(task1.get() + '-')


def set_cheng():
    task1.set(task1.get() + '*')


def set_dian():
    task1.set(task1.get() + '.')


def genhao():
    task1.set(task1.get() + '√')


def squ():
    if '+' in task1.get():
        list1 = task1.get().split('+')
        if '.' in task1.get():
            result = float(list1[0]) + float(list1[1])
        else:
            result = int(list1[0]) + int(list1[1])
        task1.set(str(result))
    elif '-' in task1.get():
        list1 = task1.get().split('-')
        if '.' in task1.get():
            result = float(list1[0]) - float(list1[1])
        else:
            result = int(list1[0]) - int(list1[1])
        task1.set(str(result))
    elif '*' in task1.get():
        list1 = task1.get().split('*')
        if '.' in task1.get():
            result = float(list1[0]) * float(list1[1])
        else:
            result = int(list1[0]) * int(list1[1])
        task1.set(str(result))
    elif '/' in task1.get():
        list1 = task1.get().split('/')
        if '.' in task1.get():
            result = float(list1[0]) / float(list1[1])
        else:
            result = int(list1[0]) / int(list1[1])
        task1.set(str(result))
    elif '√' in task1.get():
        list1 = task1.get().split('√')
        if '√' in task1.get():
            result = pow(int(list1[1]), 0.5)
            task1.set(str(result))
    else:
        pass


def clear():
    print('执行clear')
    task1.set('')


# for i in range(len(names)):
#     b = tkinter.Button(p, text=names[i], font=('Verdana', 20), width=6, command=select)
#     b.grid(row=i // 4, column=i % 4)
one = tkinter.Button(p, text='1', font=('Verdana', 20), width=6, command=set_one)
one.grid(row=0, column=0)
two = tkinter.Button(p, text='2', font=('Verdana', 20), width=6, command=set_two)
two.grid(row=0, column=1)
three = tkinter.Button(p, text='3', font=('Verdana', 20), width=6, command=set_three)
three.grid(row=0, column=2)
four = tkinter.Button(p, text='4', font=('Verdana', 20), width=6, command=set_four)
four.grid(row=1, column=0)
five = tkinter.Button(p, text='5', font=('Verdana', 20), width=6, command=set_five)
five.grid(row=1, column=1)
six = tkinter.Button(p, text='6', font=('Verdana', 20), width=6, command=set_six)
six.grid(row=1, column=2)
seven = tkinter.Button(p, text='7', font=('Verdana', 20), width=6, command=set_seven)
seven.grid(row=2, column=0)
eight = tkinter.Button(p, text='8', font=('Verdana', 20), width=6, command=set_eight)
eight.grid(row=2, column=1)
nine = tkinter.Button(p, text='9', font=('Verdana', 20), width=6, command=set_nine)
nine.grid(row=2, column=2)
ten = tkinter.Button(p, text='0', font=('Verdana', 20), width=6, command=set_ten)
ten.grid(row=3, column=0)
dian = tkinter.Button(p, text='.', font=('Verdana', 20), width=6, command=set_dian)
dian.grid(row=3, column=1)
squ = tkinter.Button(p, text='=', font=('Verdana', 20), width=6, command=squ)
squ.grid(row=3, column=2)
chu = tkinter.Button(p, text='/', font=('Verdana', 20), width=6, command=set_chu)
chu.grid(row=3, column=3)
jia = tkinter.Button(p, text='+', font=('Verdana', 20), width=6, command=set_jia)
jia.grid(row=0, column=3)
jian = tkinter.Button(p, text='-', font=('Verdana', 20), width=6, command=set_jian)
jian.grid(row=1, column=3)
cheng = tkinter.Button(p, text='*', font=('Verdana', 20), width=6, command=set_cheng)
cheng.grid(row=2, column=3)
clear = tkinter.Button(p, text='C', font=('Verdana', 20), width=6, command=clear)
clear.grid(row=4, column=0)
genhao = tkinter.Button(p, text='√', font=('Verdana', 20), width=6, command=genhao)
genhao.grid(row=4, column=1)

# b.bind('<Button-1>', select)

win.mainloop()
