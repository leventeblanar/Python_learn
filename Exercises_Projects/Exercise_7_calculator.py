from tkinter import Tk, Entry, Button, StringVar

# Tkinter - a modul in python that enables the creation of graphical applications

class Calculator:
    def __init__(self, master):
        master.title("Calculator")
        master.geometry('357x420+0+0')
        master.config(bg='grey')
        master.resizable(False, False)

        self.equation = StringVar() # Entry field - where the calculations happen visually
        self.entry_value = '' # this is the value that is being refreshed based on the equations 
        Entry(width = 17, bg = '#ccddff', font = ('Arial Bold', 28), textvariable = self.equation).place(x=0,y=0)  #self.equation is the variable that point to the below functions and those will refresh it based on the desired output

        Button(width = 11, height = 4, text='(', relief='flat', bg='white', command=lambda:self.show('(')).place(x=0, y=50)
        Button(width = 11, height = 4, text=')', relief='flat', bg='white', command=lambda:self.show(')')).place(x=90, y=50)
        Button(width = 11, height = 4, text='%', relief='flat', bg='white', command=lambda:self.show('%')).place(x=180, y=50)
        Button(width = 11, height = 4, text='1', relief='flat', bg='white', command=lambda:self.show(1)).place(x=0, y=125)
        Button(width = 11, height = 4, text='2', relief='flat', bg='white', command=lambda:self.show(2)).place(x=90, y=125)
        Button(width = 11, height = 4, text='3', relief='flat', bg='white', command=lambda:self.show(3)).place(x=180, y=125)
        Button(width = 11, height = 4, text='4', relief='flat', bg='white', command=lambda:self.show(4)).place(x=0, y=200)
        Button(width = 11, height = 4, text='5', relief='flat', bg='white', command=lambda:self.show(5)).place(x=90, y=200)
        Button(width = 11, height = 4, text='6', relief='flat', bg='white', command=lambda:self.show(6)).place(x=180, y=200)
        Button(width = 11, height = 4, text='7', relief='flat', bg='white', command=lambda:self.show(7)).place(x=0, y=275)
        Button(width = 11, height = 4, text='8', relief='flat', bg='white', command=lambda:self.show(8)).place(x=180, y=275)
        Button(width = 11, height = 4, text='9', relief='flat', bg='white', command=lambda:self.show(9)).place(x=90, y=275)
        Button(width = 11, height = 4, text='0', relief='flat', bg='white', command=lambda:self.show(0)).place(x=90, y=350)
        Button(width = 11, height = 4, text='.', relief='flat', bg='white', command=lambda:self.show('.')).place(x=180, y=350)
        Button(width = 11, height = 4, text='+', relief='flat', bg='white', command=lambda:self.show('+')).place(x=270, y=275)
        Button(width = 11, height = 4, text='-', relief='flat', bg='white', command=lambda:self.show('-')).place(x=270, y=200)
        Button(width = 11, height = 4, text='/', relief='flat', bg='white', command=lambda:self.show('/')).place(x=270, y=50)
        Button(width = 11, height = 4, text='*', relief='flat', bg='white', command=lambda:self.show('*')).place(x=270, y=125)
        Button(width = 11, height = 4, text='=', relief='flat', bg='lightblue', command=self.solve).place(x=270, y=350)
        Button(width = 11, height = 4, text='C', relief='flat', command=self.clear).place(x=0 ,y=350)

    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clear(self):  # clears the entry field by refreshing it to an empty text
        self.entry_value = ''
        self.equation.set(self.entry_value)
    
    def solve(self):
        result = eval(self.entry_value) # this eval() function does the calculations - it is capable of running string values as python code
                                        # the only downside is that eval() can run dangerous commands as well 
        self.equation.set(result )


root=Tk()
calculator=Calculator(root)
root.mainloop()