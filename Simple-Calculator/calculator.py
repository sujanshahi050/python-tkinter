
"""
File: calculator.py
Type: Class File for a Calculator Class used for Simple-Calculator project

"""

from tkinter import *

class Calculator:

	# Method to aggregate the buttons clicked
    def button_clicked(self,numbers):
        global operator
        global var
        self.operator = self.operator + str(numbers)
        self.var.set(self.operator)

    # Method to clear the entry box
    def clear(self):
        self.entry.delete(0,END)
        self.operator =""


    # Method to evaluate a given expression.
    def evaluate(self):
    	# Using eval to determine the expression and output the desired result
        self.answer = eval(self.entry.get())
        self.var.set(self.answer)
        self.operator = str(self.answer)

    # Constructor for Calculator Class
    def __init__(self,parent):
        self.operator = ""
        self.var = StringVar()

        # Creating a frame and hooking it up to the parent widget
        frame = Frame(parent, height=400, width=50 )
        frame.pack(side=TOP, fill=BOTH, expand=True)
        self.entry = Entry(frame,textvariable=self.var,bg='grey',width=50,bd=10)
        self.entry.pack()
        self.t = Text(self.entry,height=60)


        # Creating widgets and shoving them off to the screen
        label_key = Label(frame, height=35, width=50,bg='#ADB6CC')
        label_key.pack(side=LEFT, expand=True)

        label_fkey = Label(frame, height=5, width=5, bg='#334A72')
        label_fkey.pack(side=RIGHT, expand=True)

        label_7 = Label(label_key)
        label_7.grid(row=0, column=0)
        button_7 = Button(label_7, text='7',command= lambda : self.button_clicked(7))
        button_7.pack()

        label_8 = Label(label_key)
        label_8.grid(row=0, column=1)
        button_8 = Button(label_8, text='8',command= lambda: self.button_clicked(8))
        button_8.pack()

        label_9 = Label(label_key)
        label_9.grid(row=0, column=2, padx=10)
        button_9 = Button(label_9, text='9',command= lambda: self.button_clicked(9))
        button_9.pack()

        label_4 = Label(label_key)
        label_4.grid(row=1, column=0, padx=10, pady=10)
        button_4 = Button(label_4, text='4',command= lambda: self.button_clicked(4))
        button_4.pack()

        label_5 = Label(label_key)
        label_5.grid(row=1, column=1, padx=10, pady=10)
        button_5 = Button(label_5, text='5',command= lambda: self.button_clicked(5))
        button_5.pack()

        label_6 = Label(label_key)
        label_6.grid(row=1, column=2, padx=10, pady=10)
        button_6 = Button(label_6, text='6',command= lambda: self.button_clicked(6))
        button_6.pack()

        label_1 = Label(label_key)
        label_1.grid(row=2, column=0, padx=10)
        button_1 = Button(label_1, text='1',command= lambda: self.button_clicked(1))
        button_1.pack()

        label_2 = Label(label_key)
        label_2.grid(row=2, column=1, padx=10)
        button_2 = Button(label_2, text='2',command= lambda: self.button_clicked(2))
        button_2.pack()

        label_3 = Label(label_key)
        label_3.grid(row=2, column=2, padx=10)
        button_3 = Button(label_3, text='3',command= lambda: self.button_clicked(3))
        button_3.pack()

        label_0 = Label(label_key)
        label_0.grid(row=3, column=0, padx=10, pady=10)
        button_0 = Button(label_0, text='0',command= lambda: self.button_clicked(0))
        button_0.pack()

        label_decimal = Label(label_key)
        label_decimal.grid(row=3, column=1, padx=10, pady=10)
        button_decimal = Button(label_decimal, text='.',command= lambda: self.button_clicked('.'))
        button_decimal.pack()

        label_equal = Label(label_key)
        label_equal.grid(row=3, column=2, padx=10, pady=10)
        button_equal = Button(label_equal, text='=',command= self.evaluate)
        button_equal.pack()

        label_C = Label(label_fkey)
        label_C.grid(row=0, column=0,columnspan=2)
        button_C = Button(label_C, text='C', height=1, width=10,command=  self.clear)
        button_C.pack(side=LEFT)

        label_subtract = Label(label_fkey,bg='#324A6D')
        label_subtract.grid(row=1, column=0, sticky=W, pady=10)
        button_subtract = Button(label_subtract, text='-', height=1, width=3,command= lambda: self.button_clicked('-'))
        button_subtract.pack(side=LEFT)

        label_multiply = Label(label_fkey,bg='#324A6D')
        label_multiply.grid(row=1, column=1, sticky=E)
        button_multiply = Button(label_multiply, text='x', height=1, width=3,command= lambda: self.button_clicked('*'))
        button_multiply.pack()

        label_divide = Label(label_fkey,bg='#324A6D')
        label_divide.grid(row=2, column=0, sticky=W)
        button_divide = Button(label_divide, text='/', height=1, width=3,command= lambda: self.button_clicked('/'))
        button_divide.pack()

        label_add = Label(label_fkey,bg='#324A6D')
        label_add.grid(row=2, column=1, sticky=E)
        button_add = Button(label_add, text='+', height=1, width=3,command= lambda: self.button_clicked('+'))
        button_add.pack()

        label_leftBracket = Label(label_fkey,bg='#324A6D')
        label_leftBracket.grid(row=3,column=0,sticky=W,pady=10)
        button_leftBracket = Button(label_leftBracket,text='(', height=1, width=3,command= lambda: self.button_clicked('('))
        button_leftBracket.pack()

        label_rightBracket = Label(label_fkey,bg='#324A6D')
        label_rightBracket.grid(row=3, column=1, sticky=E, pady=10)
        button_rightBracket = Button(label_rightBracket, text=')', height=1, width=3,
                               command=lambda: self.button_clicked(')'))
        button_rightBracket.pack()

