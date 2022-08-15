'''

import tkinter as tk
from tkinter import *
import tkinter.font as font

gui = Tk(className='sign')
gui.geometry("500x200")
def Choose():
    myFont = font.Font(family='Courier', size=20, weight='bold')

    button_SignUp = Button(gui, text='SIGN UP', bg='#0052cc', fg='#ffffff')
    button_SignUp['font'] = myFont
    button_SignUp.pack()

    button_SignIn = Button(gui, text='SIGN IN', bg='#0052cc', fg='#ffffff')
    button_SignIn['font'] = myFont
    button_SignIn.pack()

Choose()
gui.mainloop()
'''


import tkinter as tk
from tkinter import ttk

# root window
root = tk.Tk()
root.geometry('400x300')
root.title('Notebook Demo')

# create a notebook
notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=True)

# create frames
frame1 = ttk.Frame(notebook, width=400, height=280)
frame2 = ttk.Frame(notebook, width=400, height=280)

frame1.pack(fill='both', expand=True)
frame2.pack(fill='both', expand=True)

# add frames to notebook

notebook.add(frame1, text='SIGN IN')
notebook.add(frame2, text='SIGN UP')

ttk.Widget.

root.mainloop()