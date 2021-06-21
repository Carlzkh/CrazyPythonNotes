import tkinter
from tkinter import ttk


win = tkinter.Tk()
win.title("daily to do")
win.geometry("400x400+200+10")

cv_year = tkinter.StringVar()
year = ttk.Combobox(win, textvariable=cv_year)
year.pack()
# 设置下拉数据
year['value'] = ('2018', '2019', '2020', '2021')

# 设置默认值
year.current(1)


def func(event):
    print(year.get())
    print(cv_year.get())


year.bind('<<ComboboxSelected>>',func)

year_label = tkinter.Label(win, text='年', bg='white', fg='blue',
                      font=("黑体", 20), width=2, height=1, wraplength=100, justify='left',
                      anchor='e')

year_label.pack()

cv_month = tkinter.StringVar()
month = ttk.Combobox(win, textvariable=cv_month)
month.pack()
# 设置下拉数据
month['value'] = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12')

# 设置默认值
month.current(7)


def func(event):
    print(month.get())
    print(cv_month.get())


month.bind('<<ComboboxSelected>>',func)

month_label = tkinter.Label(win, text='月', bg='white', fg='blue',
                      font=("黑体", 20), width=2, height=1, wraplength=100, justify='left',
                      anchor='s')

month_label.pack()

cv_day = tkinter.StringVar()
day = ttk.Combobox(win, textvariable=cv_day)
day.pack()
# 设置下拉数据
day['value'] = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18',
                '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31')

# 设置默认值
day.current(5)


def func(event):
    print(day.get())
    print(cv_day.get())


day.bind('<<ComboboxSelected>>',func)

day_label = tkinter.Label(win, text='日', bg='white', fg='blue',
                      font=("黑体", 20), width=2, height=1, wraplength=100, justify='left',
                      anchor='s')

day_label.pack()

task1 = tkinter.Variable()
print(task1)  # PY_VAR0
print(type(task1))

entry = tkinter.Entry(win, textvariable=task1)
entry.pack()
# e就代表输入框这个对象
# 设置值
task1.set("今日任务：")

win.mainloop()
