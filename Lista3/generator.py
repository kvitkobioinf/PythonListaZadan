import random
import json

class Game: 
    def __init__(self):
        self.plansza = [[None for i in range(10)] for j in range(10)]

    def generate(self):
        restart = False
        try:
            for i in range(5):
                for _ in range(5 - i):
                    lenght = i

                    iterations = 0
                    while True:
                        x = random.randint(0, 9)
                        y = random.randint(0, 9)
                        r = self.getRotation()
                    
                        canBreak = True
                        for k in range(lenght):
                            try:
                                if self.plansza[x + r[0] * k][y + r[1] * k] != None:
                                    canBreak = False
                            except:
                                canBreak = False

                        for k in range(lenght):
                            for a in range(8):
                                direction = self.checkDir(a)
                                try: 
                                    if self.plansza[x + r[0] * k + direction[0]][y + r[1] * k + direction[1]] != None:
                                        canBreak = False
                                except:
                                    canBreak = False

                        if canBreak:
                            break

                        iterations += 1
                    
                    if restart:
                        break

                    for k in range(lenght):
                        if k == 0:
                            self.plansza[x + r[0] * k][y + r[1] * k] = {"poprzedni": None, "nastepny": None}
                        else:
                            self.plansza[x + r[0] * k][y + r[1] * k] = {"poprzedni": [-r[0], -r[1]], "nastepny": None}
                            self.plansza[x + r[0] * (k - 1)][y + r[1] * (k - 1)]["nastepny"] = [r[0], r[1]]
                        self.plansza[x + r[0] * k][y + r[1] * k]["statek"] = False
        except:
            self.plansza = [[None for i in range(10)] for j in range(10)]
            restart = True

        if restart:
            self.generate()
                
    def getRotation(self):
        r = random.randint(0, 3)
        if r == 0:
            return [1, 0]
        elif r == 1:
            return [0, 1]
        elif r == 2:
            return [-1, 0]
        elif r == 3:
            return [0, -1]

    def checkDir(self, r):
        if r == 0:
            return [-1, 1]
        elif r == 1:
            return [0, 1]
        elif r == 2:
            return [1, 1]
        elif r == 3:
            return [1, 0]
        elif r == 4:
            return [1, -1]
        elif r == 5:
            return [0, -1]
        elif r == 6:
            return [-1, -1]
        elif r == 7:
            return [-1, 0]   

    def showJSON(self):
        print(json.dumps(self.plansza))

if __name__ == "__main__":
    g = Game()
    g.generate()
    g.showJSON()