from tkinter import *
import math
import sqlite3
from datetime import date, datetime
import random

class Leaderboards(object):
    def __init__(self, master):
        top = self.top = Toplevel(master)
        self.sql()
        self.l = Text(top)
        self.l.insert(END, self.rows)

        self.l.pack()

    def sql(self):
        conn = sqlite3.connect('toto-lotek.db')

        c = conn.cursor()
        c.execute("SELECT * from leaderboards")

        self.rows = c.fetchall()
        text = ""
        for data in self.rows:
            for part in data:
                text += part + " "
            text += "\n"
        self.rows = text

        conn.commit()
        conn.close()

    def cleanup(self):
        self.top.destroy()

class addToLeaderboards(object):
    def __init__(self, master, text):
        self.text = text
        top = self.top = Toplevel(master)
        self.l = Label(top, text = self.text)
        self.e = Entry(top)
        self.b = Button(top, text="Zapisz wynik", command = self.cleanup)

        self.l.pack()
        self.e.pack()
        self.b.pack()

    def sql(self, name):
        dzien = date.today().strftime("%d-%m-%Y")
        czas = datetime.now().strftime("%H:%M:%S")
        conn = sqlite3.connect('toto-lotek.db')

        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS leaderboards (data text, time text, name text, wynik text)")
        
        c.execute("INSERT INTO leaderboards(dzien, godzin, gracz, wynik) VALUES ('" + dzien + "', '" + czas + "', '" + name + "', '" + self.text + "')")

        conn.commit()
        conn.close()

    def cleanup(self):
        self.value = self.e.get()
        self.sql(self.value)
        self.top.destroy()

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
        self.text = str(v) + "/6"
        self.addTo()

    def generate(self):
        for x in range(0, 49):
            self.otherStuff.append(Checkbutton(self.master, text=str(x + 1), variable = self.variables[x], command = self.showAll))

        self.stuffToScreen.append(Button(self.master, text="Sprawdź swój wynik", command=self.check))
        self.stuffToScreen.append(Button(self.master, text="Najlpesze wyniki", command=self.leaderboards))

        columns = 6

        for x in range(len(self.otherStuff)):
            if not x % columns:
                self.otherStuff[x].grid(row=math.floor(x / columns) * columns, column=0)
            else:
                self.otherStuff[x].grid(row=math.floor(x / columns) * columns, column=x % columns)

        for i in range(len(self.stuffToScreen)):
            x = len(self.otherStuff) + x % columns + 1 + i
            self.stuffToScreen[i].grid(row=math.floor(x / columns) * columns + 1, column=columns - i + 1)

    def leaderboards(self):
        self.w = Leaderboards(self.master)
        self.stuffToScreen[0]["state"] = "disabled" 
        self.master.wait_window(self.w.top)
        self.stuffToScreen[0]["state"] = "normal"
    
    def addTo(self):
        self.w = addToLeaderboards(self.master, self.text)
        self.stuffToScreen[1]["state"] = "disabled" 
        self.master.wait_window(self.w.top)
        self.stuffToScreen[1]["state"] = "normal"

    def entryValue(self):
        print(self.w.value)
        return self.w.value

if __name__ == "__main__":
    root = Tk()
    m = mainWindow(root)
    root.mainloop()