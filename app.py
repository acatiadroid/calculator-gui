# No libraries need to be imported!

import tkinter as tk
from tkinter import *
from operator import add, sub, truediv, mul
import tkinter.font as font

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.ls = []
    
        self.pack(fill=BOTH, expand=1)

        myFont = font.Font(size='20')
        labelFont = font.Font(size='13')
        
        self.inputLabel = Label(self, text='Input shown here  ', bg='grey17', fg='white')
        self.inputLabel.place(x=95, y=20)
        self.inputLabel["font"] = labelFont

        self.outputLabel = Label(self, text='Output shown here', bg='grey17', fg='white')
        self.outputLabel.place(x=95, y=55)
        self.outputLabel["font"] = labelFont

        inputText = Label(self, text='Input   :', bg='grey17', fg='white')
        inputText.place(x=30, y=20)
        inputText["font"] = labelFont

        outputText = Label(self, text='Output : ', bg='grey17', fg='white')
        outputText.place(x=30, y=55)
        outputText["font"] = labelFont

        buttonSeven = Button(self, text=' 7 ', command=self.appendSeven, bg='grey60', fg='black', borderwidth=0)
        buttonSeven.place(x=10, y=90)
        buttonSeven["font"] = myFont

        buttonEight = Button(self, text=' 8 ', command=self.appendEight, bg='grey60', fg='black', borderwidth=0)
        buttonEight.place(x=70, y=90)
        buttonEight["font"] = myFont
        
        buttonNine = Button(self, text=' 9 ', command=self.appendNine, bg='grey60', fg='black', borderwidth=0)
        buttonNine.place(x=130, y=90)
        buttonNine["font"] = myFont

        buttonFour = Button(self, text=' 4 ', command=self.appendFour, bg='grey60', fg='black', borderwidth=0)
        buttonFour.place(x=10, y=150)
        buttonFour["font"] = myFont

        buttonFive = Button(self, text=' 5 ', command=self.appendFive, bg='grey60', fg='black', borderwidth=0)
        buttonFive.place(x=70, y=150)
        buttonFive["font"] = myFont

        buttonSix = Button(self, text=' 6 ', command=self.appendSix, bg='grey60', fg='black', borderwidth=0)
        buttonSix.place(x=130, y=150)
        buttonSix["font"] = myFont

        buttonOne = Button(self, text=' 1 ', command=self.appendOne, bg='grey60', fg='black', borderwidth=0)
        buttonOne.place(x=10, y=210)
        buttonOne["font"] = myFont

        buttonTwo = Button(self, text=' 2 ', command=self.appendTwo, bg='grey60', fg='black', borderwidth=0)
        buttonTwo.place(x=70, y=210)
        buttonTwo["font"] = myFont

        buttonThree = Button(self, text=' 3 ', command=self.appendThree, bg='grey60', fg='black', borderwidth=0)
        buttonThree.place(x=130, y=210)
        buttonThree["font"] = myFont
    
        buttonEnter = Button(self, text=' = ', command=self.enter, bg='LightBlue3', fg='black', borderwidth=0)
        buttonEnter.place(x=130, y=270)
        buttonEnter["font"] = myFont
        
        buttonZero = Button(self, text=' 0 ', command=self.appendZero, bg='grey60', fg='black', borderwidth=0)
        buttonZero.place(x=70, y=270)
        buttonZero["font"] = myFont

        buttonAdd = Button(self, text=' + ', command=self.add, bg='grey30', fg='white', borderwidth=0)
        buttonAdd.place(x=190, y=90)
        buttonAdd["font"] = myFont
        
        buttonClear = Button(self, text='Clear', command=self.clearCalc, bg='grey30', fg='white', borderwidth=0)
        buttonClear.place(x=250, y=90)
        buttonClear["font"] = labelFont
        
        buttonSubtract = Button(self, text=' -  ', command=self.subtract, bg='grey30', fg='white', borderwidth=0)
        buttonSubtract.place(x=190, y=150)
        buttonSubtract["font"] = myFont

        buttonDivide = Button(self, text=' ÷ ', command=self.divide, bg='grey30', fg='white', borderwidth=0)
        buttonDivide.place(x=190, y=210)
        buttonDivide["font"] = myFont

        buttonMultiply = Button(self, text=' × ', command=self.multiply, bg='grey30', fg='white', borderwidth=0)
        buttonMultiply.place(x=190, y=270)
        buttonMultiply["font"] = myFont
    
    def add(self):
        self.ls.append('+')
        self.inputLabel.configure(text=''.join(str(v) for v in self.ls), bg='grey17', fg='white')
    
    def subtract(self):
        self.ls.append('-')
        self.inputLabel.configure(text=''.join(str(v) for v in self.ls), bg='grey17', fg='white')
    
    def divide(self):
        self.ls.append('/')
        self.inputLabel.configure(text=''.join(str(v) for v in self.ls), bg='grey17', fg='white')
    
    def multiply(self):
        self.ls.append('*')
        self.inputLabel.configure(text=''.join(str(v) for v in self.ls), bg='grey17', fg='white')

    def appendZero(self):
        self.ls.append(0)
        self.inputLabel.configure(text=''.join(str(v) for v in self.ls), bg='grey17', fg='white')
    
    def appendOne(self):
        self.ls.append(1)
        self.inputLabel.configure(text=''.join(str(v) for v in self.ls), bg='grey17', fg='white')

    def appendTwo(self):
        self.ls.append(2)
        self.inputLabel.configure(text=''.join(str(v) for v in self.ls), bg='grey17', fg='white')
    
    def appendThree(self):
        self.ls.append(3)
        self.inputLabel.configure(text=''.join(str(v) for v in self.ls), bg='grey17', fg='white')
    
    def appendFour(self):
        self.ls.append(4)
        self.inputLabel.configure(text=''.join(str(v) for v in self.ls), bg='grey17', fg='white')
    
    def appendFive(self):
        self.ls.append(5)
        self.inputLabel.configure(text=''.join(str(v) for v in self.ls), bg='grey17', fg='white')
    
    def appendSix(self):
        self.ls.append(6)
        self.inputLabel.configure(text=''.join(str(v) for v in self.ls), bg='grey17', fg='white')
    
    def appendSeven(self):
        self.ls.append(7)
        self.inputLabel.configure(text=''.join(str(v) for v in self.ls), bg='grey17', fg='white')
    
    def appendEight(self):
        self.ls.append(8)
        self.inputLabel.configure(text=''.join(str(v) for v in self.ls), bg='grey17', fg='white')
    
    def appendNine(self):
        self.ls.append(9)
        self.inputLabel.configure(text=''.join(str(v) for v in self.ls), bg='grey17', fg='white')
    
    def enter(self):
        if not self.ls:
            return self.outputLabel.configure(text='You didn\'t enter anything...')
        
        try:
            ans = eval(''.join(str(x) for x in self.ls))
            ans = "{:,}".format(ans)
        except ZeroDivisionError:
            return self.outputLabel.configure(text='You cannot divide by zero', bg='grey17', fg='white')
        except SyntaxError:
            return self.outputLabel.configure(text='SyntaxError', bg='grey17', fg='white')
        except Exception:
            return self.outputLabel.configure(text='Error', bg='grey17', fg='white')

        self.outputLabel.configure(text=ans)
    
    def clearCalc(self):
        self.ls.clear()
        self.inputLabel.configure(text='Input shown here  ', bg='grey17', fg='white')
        self.outputLabel.configure(text='Output shown here', bg='grey17', fg='white')
    

if __name__ == "__main__":
    root = Tk()
    app = Window(root)
    app.configure(bg='grey17')
    root.wm_title('Calculator')
    root.iconbitmap(r'calc.ico')
    root.geometry("320x350")
    root.mainloop()

