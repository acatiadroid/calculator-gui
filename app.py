from tkinter import *
import tkinter.font as font

import os # For checking if the "calc.ico" exists

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.ls = []
    
        self.pack(fill=BOTH, expand=1)

        myFont = font.Font(size='20')
        labelFont = font.Font(size='13')
        operatorFont = font.Font(size='12')

    # Input and output labels for displaying input & output

        self.inputLabel = Label(self, text='Input shown here  ', bg='grey17', fg='white')
        self.inputLabel.place(x=95, y=20)
        self.inputLabel["font"] = labelFont

        self.outputLabel = Label(self, text='Output shown here', bg='grey17', fg='white')
        self.outputLabel.place(x=95, y=55)
        self.outputLabel["font"] = labelFont


    # Headers for input & output labels

        self.inputText = Label(self, text='Input   :', bg='grey17', fg='white')
        self.inputText.place(x=30, y=20)
        self.inputText["font"] = labelFont

        self.outputText = Label(self, text='Output : ', bg='grey17', fg='white')
        self.outputText.place(x=30, y=55)
        self.outputText["font"] = labelFont


    # Buttons for inputting numbers

        self.buttonNine = Button(self, text=' 9 ', command=lambda: self.appendInt(9), bg='grey60', fg='black')
        self.buttonNine.place(x=130, y=90)
        self.buttonNine["font"] = myFont

        self.buttonEight = Button(self, text=' 8 ', command=lambda: self.appendInt(8), bg='grey60', fg='black')
        self.buttonEight.place(x=70, y=90)
        self.buttonEight["font"] = myFont

        self.buttonSeven = Button(self, text=' 7 ', command=lambda: self.appendInt(7), bg='grey60', fg='black')
        self.buttonSeven.place(x=10, y=90)
        self.buttonSeven["font"] = myFont
        
        self.buttonSix = Button(self, text=' 6 ', command=lambda: self.appendInt(6), bg='grey60', fg='black')
        self.buttonSix.place(x=130, y=150)
        self.buttonSix["font"] = myFont

        self.buttonFive = Button(self, text=' 5 ', command=lambda: self.appendInt(5), bg='grey60', fg='black')
        self.buttonFive.place(x=70, y=150)
        self.buttonFive["font"] = myFont

        self.buttonFour = Button(self, text=' 4 ', command=lambda: self.appendInt(4), bg='grey60', fg='black')
        self.buttonFour.place(x=10, y=150)
        self.buttonFour["font"] = myFont

        self.buttonThree = Button(self, text=' 3 ', command=lambda: self.appendInt(3), bg='grey60', fg='black')
        self.buttonThree.place(x=130, y=210)
        self.buttonThree["font"] = myFont

        self.buttonTwo = Button(self, text=' 2 ', command=lambda: self.appendInt(2), bg='grey60', fg='black')
        self.buttonTwo.place(x=70, y=210)
        self.buttonTwo["font"] = myFont

        self.buttonOne = Button(self, text=' 1 ', command=lambda: self.appendInt(1), bg='grey60', fg='black')
        self.buttonOne.place(x=10, y=210)
        self.buttonOne["font"] = myFont
        
        self.buttonZero = Button(self, text=' 0 ', command=lambda: self.appendInt(0), bg='grey60', fg='black')
        self.buttonZero.place(x=70, y=270)
        self.buttonZero["font"] = myFont


    # Buttons for inputting operators

        self.buttonAdd = Button(self, text=' + ', command=lambda: self.appendOperator("+"), bg='grey30', fg='white')
        self.buttonAdd.place(x=190, y=90)
        self.buttonAdd["font"] = myFont

        self.buttonSubtract = Button(self, text=' -  ', command=lambda: self.appendOperator("-"), bg='grey30', fg='white')
        self.buttonSubtract.place(x=190, y=150)
        self.buttonSubtract["font"] = myFont

        self.buttonDivide = Button(self, text=' ÷ ', command=lambda: self.appendOperator("/"), bg='grey30', fg='white')
        self.buttonDivide.place(x=190, y=210)
        self.buttonDivide["font"] = myFont

        self.buttonMultiply = Button(self, text=' × ', command=lambda: self.appendOperator("*"), bg='grey30', fg='white')
        self.buttonMultiply.place(x=190, y=270)
        self.buttonMultiply["font"] = myFont
        
        self.buttonDecimal = Button(self, text=' . ', command=lambda: self.appendOperator("."), bg='grey30', fg='white', height=1, width=2)
        self.buttonDecimal.place(x=250, y=150)
        self.buttonDecimal["font"] = myFont

        self.buttonOpenBracket = Button(self, text=' ( ', command=lambda: self.appendOperator("("), bg='grey50', fg='white')
        self.buttonOpenBracket.place(x=10, y=270)
        self.buttonOpenBracket["font"] = operatorFont

        self.buttonClosedBracket = Button(self, text=' ) ', command=lambda: self.appendOperator(")"), bg='grey50', fg='white')
        self.buttonClosedBracket.place(x=40, y=270)
        self.buttonClosedBracket["font"] = operatorFont

        
    # Buttons for calculator functions

        self.buttonClear = Button(self, text='Clear', command=self.clearCalc, bg='grey30', fg='white')
        self.buttonClear.place(x=250, y=90)
        self.buttonClear["font"] = labelFont

        self.buttonEnter = Button(self, text=' = ', command=self.enter, bg='LightBlue3', fg='black')
        self.buttonEnter.place(x=130, y=270)
        self.buttonEnter["font"] = myFont

    
    # Methods
    
    def updateLabel(self):
        self.inputLabel.configure(text=''.join(str(v) for v in self.ls), bg='grey17', fg='white')

    def appendOperator(self, op):
        self.ls.append(op)
        self.updateLabel()

    def appendInt(self, number):
        self.ls.append(number)
        self.updateLabel()

    def enter(self):
        if not self.ls:
            return self.outputLabel.configure(text='You didn\'t enter anything', bg='grey17', fg='red')
        
        try:
            ans = eval(''.join(str(x) for x in self.ls))
            ans = "{:,}".format(ans)
        except ZeroDivisionError:
            return self.outputLabel.configure(text='You cannot divide by zero', bg='grey17', fg='red')
        except SyntaxError:
            return self.outputLabel.configure(text='SyntaxError', bg='grey17', fg='red')
        except Exception:
            return self.outputLabel.configure(text='Error', bg='grey17', fg='red')
        
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
    if os.path.exists('./calc.ico'):
        root.iconbitmap(r'calc.ico')
    root.geometry("320x400")
    root.mainloop()