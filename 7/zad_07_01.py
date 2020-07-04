from tkinter import *
import math
import random
from tkinter import messagebox

class mainWindow(object):
    def __init__(self, master):
        self.master = master
        self.master.title("Toto-Lotek")

        self.otherStuff = []
        self.stuffToScreen = []

        self.variables = [IntVar() for _ in range(49)]
        self.text = ""
        self.generate()

    def showAll(self):
        v = 0
        for x in range(len(self.variables)):
            v += self.variables[x].get()
            if not v <= 6:
                self.variables[x].set(0)
            
    def check(self):
        numbers = [random.randint(0, 48) for _ in range(6)]
        v = 0
        for x in numbers:
            v += self.variables[x].get()
        messagebox.showinfo("Twój wynik", str(v) + " poprawnych skreśleń (z 6 możliwych)")

    def generate(self):
        for x in range(0, 49):
            self.otherStuff.append(Checkbutton(self.master, text=str(x + 1), variable = self.variables[x], command = self.showAll))

        self.stuffToScreen.append(Button(self.master, text="Sprawdź swój wynik", command=self.check))

        columns = 6

        for x in range(len(self.otherStuff)):
            if not x % columns:
                self.otherStuff[x].grid(row=math.floor(x / columns) * columns, column=0)
            else:
                self.otherStuff[x].grid(row=math.floor(x / columns) * columns, column=x % columns)

        for i in range(len(self.stuffToScreen)):
            x = len(self.otherStuff) + x % columns + 1 + i
            self.stuffToScreen[i].grid(row=math.floor(x / columns) * columns + 1, column=columns - i + 1)

    def entryValue(self):
        print(self.w.value)
        return self.w.value

if __name__ == "__main__":
    root = Tk()
    m = mainWindow(root)
    root.mainloop()