import sys

KLUCZ = 5

def szyfruj(tekst):
    zaszyfrowny = ""
    for znak in tekst:
        zaszyfrowny += chr(ord(znak) + KLUCZ)
    return zaszyfrowny

def rozszyfruj(tekst):
    odszyfrowany = ""
    for znak in tekst:
        odszyfrowany += chr(ord(znak) - KLUCZ)
    return odszyfrowany

args = sys.argv
if '--decode' in args:
    tekst = input("Podaj tekst do rozszyfrowania: \n")
    print("Tekst rozszyfrowany: " + rozszyfruj(tekst))
else:
    tekst = input("Podaj tekst do zaszyfrowania: \n")
    print("Tekst zaszyfrowany: " + szyfruj(tekst))