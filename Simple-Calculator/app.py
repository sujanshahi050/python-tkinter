
#! usr/bin/env python3

"""
File: app.py
Type: Main File that imports a Calculator Class and creates a Tk Window and then shoves that Calculator object into the root widget

"""
from tkinter import *

from calculator import Calculator

root = Tk()
root.title("Calculator")


calculator = Calculator(root)

root.mainloop()