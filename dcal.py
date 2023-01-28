#библиотеки
from tkinter import *

#функции
def set_value(formula):
    if formula == '':
        lbl['text']='0'
    else:
        lbl['text']=str(eval(formula))
def logicalc(operation):
    if operation == "C":
        set_value('')
    elif operation == "DEL":
        set_value(lbl['text'][0:-1])
    elif operation == "X^2":
        set_value(str((eval(lbl["text"]))**2))
    elif operation == "=":
        set_value(lbl["text"])
    else:
        if lbl['text'] == "0":
            lbl["text"] =''
        lbl["text"] = lbl['text']+operation

#переменные/массивы
btns = [
"C", "DEL", "*", "=",
"1", "2", "3", "/",
"4", "5", "6", "+", 
"7", "8", "9", "-",
"(", "0", ")", "X^2"
]

#основа
root = Tk()
root["bg"] = "black"
root.geometry("485x550+200+200")
root.title("Калькулятор")
root.resizable(False, False)
lbl = Label(text='0', font=("Consolas", 21, "bold"), bg="black", foreground="white")
lbl.place(x=11, y=50)
x = 10
y = 140
for bt in btns:
    com = lambda x=bt: logicalc(x)
    Button(text=bt, bg="white", font=("Consolas", 15), command=com). place(x=x,y=y ,width=115, heigh=79)
    x += 117
    if x > 400:
        x = 10
        y += 81
root.mainloop()