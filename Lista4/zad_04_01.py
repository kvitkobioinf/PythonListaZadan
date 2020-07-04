class RomanParse:
    def __init__(self, liczba):
        self.slownik = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'),
                        (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

        if int == type(liczba):
            self.arabska = liczba
            self.rzymska = self.naArabska()
        else:
            self.rzymska = liczba
            self.arabska = self.naRzymska()

    def naRzymska(self):
        rzymska = 0
        for i in range(0, len(self.rzymska)):
            for each in self.slownik:
                if self.rzymska[i] == each[1]:
                    if each[0] > rzymska:
                        rzymska = each[0] - rzymska
                    else:
                        rzymska = rzymska + each[0]

        return rzymska

    def naArabska(self):
        arabska = self.arabska
        result = ''
        for denom, rzymski_znak in self.slownik:
            result += rzymski_znak * int((arabska / denom))
            arabska %= denom
        return result


if __name__ == "__main__":
    print('Konwersja na liczbę rzymską. Podaj liczbę arabską (np. 64)')
    arabska = int(input())
    print('Liczba rzymska: ' + RomanParse(arabska).rzymska)
    print()

    print('Konwersja na liczbę arabską. Podaj liczbę rzymską (np. IV)')
    rzymska = input()
    print('Liczba arabska: ' + str(RomanParse(rzymska).arabska))
