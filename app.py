# No libraries need to be imported!

from tkinter import *
from operator import add, sub, truediv, mul
import tkinter.font as font

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.ls = []
        self.operations = {"+": add, "-": sub, "/": truediv, "*": mul}
    
        self.pack(fill=BOTH, expand=1)

        myFont = font.Font(size='20')
        labelFont = font.Font(size='13')
        exitFont = font.Font(size='10')
        
        self.inputLabel = Label(self, text='Input shown here  ')
        self.inputLabel.place(x=30, y=30)
        self.inputLabel["font"] = labelFont

        self.outputLabel = Label(self, text='Output shown here')
        self.outputLabel.place(x=30, y=60)
        self.outputLabel["font"] = labelFont

        buttonExit = Button(self, text='Exit', command=self.clickExitButton)
        buttonExit.place(x=0, y=0)
        buttonExit["font"] = exitFont

        buttonSeven = Button(self, text=' 7 ', command=self.appendSeven)
        buttonSeven.place(x=10, y=90)
        buttonSeven["font"] = myFont

        buttonEight = Button(self, text=' 8 ', command=self.appendEight)
        buttonEight.place(x=70, y=90)
        buttonEight["font"] = myFont
        
        buttonNine = Button(self, text=' 9 ', command=self.appendNine)
        buttonNine.place(x=130, y=90)
        buttonNine["font"] = myFont

        buttonFour = Button(self, text=' 4 ', command=self.appendFour)
        buttonFour.place(x=10, y=150)
        buttonFour["font"] = myFont

        buttonFive = Button(self, text=' 5 ', command=self.appendFive)
        buttonFive.place(x=70, y=150)
        buttonFive["font"] = myFont

        buttonSix = Button(self, text=' 6 ', command=self.appendSix)
        buttonSix.place(x=130, y=150)
        buttonSix["font"] = myFont

        buttonOne = Button(self, text=' 1 ', command=self.appendOne)
        buttonOne.place(x=10, y=210)
        buttonOne["font"] = myFont

        buttonTwo = Button(self, text=' 2 ', command=self.appendTwo)
        buttonTwo.place(x=70, y=210)
        buttonTwo["font"] = myFont

        buttonThree = Button(self, text=' 3 ', command=self.appendThree)
        buttonThree.place(x=130, y=210)
        buttonThree["font"] = myFont
    
        buttonEnter = Button(self, text=' = ', command=self.enter)
        buttonEnter.place(x=130, y=270)
        buttonEnter["font"] = myFont
        
        buttonZero = Button(self, text=' 0 ', command=self.appendZero)
        buttonZero.place(x=70, y=270)
        buttonZero["font"] = myFont

        buttonAdd = Button(self, text=' + ', command=self.add)
        buttonAdd.place(x=190, y=90)
        buttonAdd["font"] = myFont
        
        buttonClear = Button(self, text='Clear', command=self.clearCalc)
        buttonClear.place(x=250, y=90)
        buttonClear["font"] = labelFont
        
        buttonSubtract = Button(self, text=' -  ', command=self.subtract)
        buttonSubtract.place(x=190, y=150)
        buttonSubtract["font"] = myFont

        buttonDivide = Button(self, text=' ÷ ', command=self.divide)
        buttonDivide.place(x=190, y=210)
        buttonDivide["font"] = myFont

        buttonMultiply = Button(self, text=' × ', command=self.multiply)
        buttonMultiply.place(x=190, y=270)
        buttonMultiply["font"] = myFont
    
    def clickExitButton(self):
        exit()

    def add(self):
        self.ls.append('+')
        self.inputLabel.configure(text=''.join(str(v) for v in self.ls))
    
    def subtract(self):
        self.ls.append('-')
        self.inputLabel.configure(text=''.join(str(v) for v in self.ls))
    
    def divide(self):
        self.ls.append('/')
        self.inputLabel.configure(text=''.join(str(v) for v in self.ls))
    
    def multiply(self):
        self.ls.append('*')
        self.inputLabel.configure(text=''.join(str(v) for v in self.ls))

    def appendZero(self):
        self.ls.append(0)
        self.inputLabel.configure(text=''.join(str(v) for v in self.ls))
    
    def appendOne(self):
        self.ls.append(1)
        self.inputLabel.configure(text=''.join(str(v) for v in self.ls))

    def appendTwo(self):
        self.ls.append(2)
        self.inputLabel.configure(text=''.join(str(v) for v in self.ls))
    
    def appendThree(self):
        self.ls.append(3)
        self.inputLabel.configure(text=''.join(str(v) for v in self.ls))
    
    def appendFour(self):
        self.ls.append(4)
        self.inputLabel.configure(text=''.join(str(v) for v in self.ls))
    
    def appendFive(self):
        self.ls.append(5)
        self.inputLabel.configure(text=''.join(str(v) for v in self.ls))
    
    def appendSix(self):
        self.ls.append(6)
        self.inputLabel.configure(text=''.join(str(v) for v in self.ls))
    
    def appendSeven(self):
        self.ls.append(7)
        self.inputLabel.configure(text=''.join(str(v) for v in self.ls))
    
    def appendEight(self):
        self.ls.append(8)
        self.inputLabel.configure(text=''.join(str(v) for v in self.ls))
    
    def appendNine(self):
        self.ls.append(9)
        self.inputLabel.configure(text=''.join(str(v) for v in self.ls))
    
    def enter(self):
        if not self.ls:
            return self.outputLabel.configure(text='You didn\'t enter anything...')
        
        try:
            ans = eval(''.join(str(x) for x in self.ls))
        except ZeroDivisionError:
            return self.outputLabel.configure(text='You cannot divide by zero')
        except SyntaxError:
            return self.outputLabel.configure(text='SyntaxError')
        except Exception:
            return self.outputLabel.configure(text='Error')

        self.outputLabel.configure(text=ans)
    
    def clearCalc(self):
        self.ls.clear()
        self.inputLabel.configure(text='Input shown here  ')
        self.outputLabel.configure(text='Output shown here')
    

if __name__ == "__main__":
    root = Tk()
    app = Window(root)
    app.configure(bg='grey')
    root.wm_title('Calculator')
    root.geometry("320x350")
    root.mainloop()

