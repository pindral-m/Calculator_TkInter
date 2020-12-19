from tkinter import *
from tkinter import messagebox

calc = Tk()
calc.title("Kalkulator v.0.1")
calc.resizable(0, 0)

class Application(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.CreateWidgets()

    def Calculation(self):
        self.calculation = self.display.get()
        self.calculation = self.calculation.replace("%", "/100")
        try:
            self.result = eval(self.calculation)
            self.Replace(self.result)
        except:
            messagebox.showinfo("Błąd!", "Wprowadzono nieprawidłowe dane!")

    def Replace(self, text):
        self.display.delete(0, END)
        self.display.insert(0, text)

    def Append(self, text):
        self.entryText = self.display.get()
        self.textLenght = len(self.entryText)

        if self.entryText == "0":
            self.Replace(text)
        else:
            self.display.insert(self.textLenght, text)

    def Remove(self):
        actual_state = self.display.get()
        new_state = actual_state[:len(actual_state)-1]
        self.Replace(new_state)

    def Clear(self):
        self.Replace("0")

    def CreateWidgets(self):
        self.display = Entry(self, font=("Helvetica", 16), borderwidth=0, relief=RAISED, justify=RIGHT)
        self.display.insert(0, "0")
        self.display.grid(row=0, column=0, columnspan=5)

        self.Seven = Button(self, font=("Helvetica", 11), text="7", borderwidth=1, command=lambda: self.Append("7"))
        self.Seven.grid(row=1, column=0, sticky="NWNSWSE")

        self.Eight = Button(self, font=("Helvetica", 11), text="8", borderwidth=1, command=lambda: self.Append("8"))
        self.Eight.grid(row=1, column=1, sticky="NWNESWSE")

        self.Nine = Button(self, font=("Helvetica", 11), text="9", borderwidth=1, command=lambda: self.Append("9"))
        self.Nine.grid(row=1, column=2, sticky="NWNESWSE")

        self.Plus = Button(self, font=("Helvetica", 11), text="+", borderwidth=1, command=lambda: self.Append("+"))
        self.Plus.grid(row=1, column=3, sticky="NWNESWSE")

        self.Clear = Button(self, font=("Helvetica", 11), text="CE", borderwidth=1, command=self.Clear)
        self.Clear.grid(row=1, column=4, sticky="NWNESWSE")

        self.Four = Button(self, font=("Helvetica", 11), text="4", borderwidth=1, command=lambda: self.Append("4"))
        self.Four.grid(row=2, column=0, sticky="NWNESWSE")

        self.Five = Button(self, font=("Helvetica", 11), text="5", borderwidth=1, command=lambda: self.Append("5"))
        self.Five.grid(row=2, column=1, sticky="NWNESWSE")

        self.Six = Button(self, font=("Helvetica", 11), text="6", borderwidth=1, command=lambda: self.Append("6"))
        self.Six.grid(row=2, column=2, sticky="NWNESWSE")

        self.Minus = Button(self, font=("Helvetica", 11), text="-", borderwidth=1, command=lambda: self.Append("-"))
        self.Minus.grid(row=2, column=3, sticky="NWNESWSE")

        self.Remove = Button(self, font=("Helvetica", 11), text="⌫", borderwidth=1, command=self.Remove)
        self.Remove.grid(row=2, column=4, sticky="NWNESWSE")

        self.One = Button(self, font=("Helvetica", 11), text="1", borderwidth=1, command=lambda: self.Append("1"))
        self.One.grid(row=3, column=0, sticky="NWNESWSE")

        self.Two = Button(self, font=("Helvetica", 11), text="2", borderwidth=1, command=lambda: self.Append("2"))
        self.Two.grid(row=3, column=1, sticky="NWNESWSE")

        self.Three = Button(self, font=("Helvetica", 11), text="3", borderwidth=1, command=lambda: self.Append("3"))
        self.Three.grid(row=3, column=2, sticky="NWNESWSE")

        self.Multiply = Button(self, font=("Helvetica", 11), text="*", borderwidth=1, command=lambda: self.Append("*"))
        self.Multiply.grid(row=3, column=3, sticky="NWNESWSE")

        self.Equal = Button(self, font=("Helvetica", 11), text="=", borderwidth=1, command=lambda: self.Calculation())
        self.Equal.grid(row=3, column=4, rowspan=2, sticky="NWNESWSE")

        self.Dot = Button(self, font=("Helvetica", 11), text=".", borderwidth=1, command=lambda: self.Append("."))
        self.Dot.grid(row=4, column=0, sticky="NWNESWSE")

        self.Zero = Button(self, font=("Helvetica", 11), text="0", borderwidth=1, command=lambda: self.Append("0"))
        self.Zero.grid(row=4, column=1, sticky="NWNESWSE")

        self.Percent = Button(self, font=("Helvetica", 11), text="%", borderwidth=1, command=lambda: self.Append("%"))
        self.Percent.grid(row=4, column=2, sticky="NWNESWSE")

        self.Divide = Button(self, font=("Helvetica", 11), text="/", borderwidth=1, command=lambda: self.Append("/"))
        self.Divide.grid(row=4, column=3, sticky="NWNESWSE")


app = Application(calc).grid()

calc.mainloop()
