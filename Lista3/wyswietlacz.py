import sys
import json

class Game: 
    def __init__(self, text):
        self.plansza = json.loads(text)
    
    def show(self):
        sys.stdout.write("\t")
        for x in range(0, 10):
            sys.stdout.write(chr(65 + x) + " ")
        sys.stdout.write("\n")
        i = 1
        for x in self.plansza:
            if i > 9:
                sys.stdout.write(str(i) + "\t")
            else:
                sys.stdout.write("0" + str(i) + "\t")
            i += 1
            for y in x:
                if y == None:
                    sys.stdout.write("=")
                elif y == "+":
                    sys.stdout.write("+")
                elif y["statek"]:
                    sys.stdout.write("x")
                else:
                    sys.stdout.write("o")
                sys.stdout.write(" ")
            sys.stdout.write("\n")

if __name__ == "__main__":
    args = sys.stdin.readline()
    if len(args) != 0:
        game = Game(args)
        game.show()