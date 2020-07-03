import sys
import json

class Game: 
    def __init__(self, text):
        self.plansza = json.loads(text)
        self.end = False
    
    def check(self, x, y, i = 0):
        state = True
        state1 = True
        try:
            cords = self.plansza[x][y]["next"]
            cords2 = self.plansza[x][y]["previous"]
            if i < 2:
                if cords != None:
                    if self.check(cords[0] + x, cords[1] + y, i + 1) and self.plansza[x][y]["hit"]:
                        state = True
                    else:
                        state = False

                if cords2 != None:
                    if self.check(cords2[0] + x, cords2[1] + y, i + 1) and self.plansza[x][y]["hit"]:
                        state1 = True
                    else:
                        state1 = False

            return state * state1
        except:
            return True

    def checkAll(self):
        b = True
        for x in range(len(self.plansza)):
            for y in range(len(self.plansza[x])):
                
                if self.plansza[x][y] != None:
                    b = b * self.plansza[x][y]["hit"]
        return b

    def shoot(self):
        while True:
            if self.checkAll():
                self.end = True
                break

            try:
                sys.stdout.write("Wykonaj ruch np. (A10): \n")
                line = sys.stdin.readline()
                line = line.replace(" ", "").replace("\n", "").replace("\t", "")
                if len(line) == 3:
                    try:
                        if ord(line[0]) - 65 >= 0 and ord(line[0]) - 65 < 10 and int(line[1] + line[2]) > 0 and int(line[1] + line[2]) <= 10:
                            if self.plansza[int(line[1] + line[2]) - 1][ord(line[0]) - 65] == None:
                                self.plansza[int(line[1] + line[2]) - 1][ord(line[0]) - 65] = "+"
                                sys.stdout.write("pudło\n")
                            else: 
                                self.plansza[int(line[1] + line[2]) - 1][ord(line[0]) - 65]["hit"] = True
                                if self.check(int(line[1] + line[2]) - 1, ord(line[0]) - 65):
                                    sys.stdout.write("zatopiony\n")
                                else:
                                    sys.stdout.write("trafiony\n")
                            break
                        else:
                            sys.stdout.write("błąd\n")
                    except:
                        sys.stdout.write("błąd\n")
            except EOFError:
                sys.stdout.write("No eof'ing\n")
            except KeyboardInterrupt:
                sys.stdout.write("No quitting till end\n")
            else:
                sys.stdout.write("błąd\n")

            
            

if __name__ == "__main__":
    args = sys.argv
    args.pop(0)
    if len(args) != 0:
        with open(args[0], "r") as f:
            text = f.read().replace("\x00", "").replace("\xff\xfe", "")
            game = Game(text)
            while True:
                game.shoot()
                if game.end:
                    sys.stdout.write("koniec\n")
                    break