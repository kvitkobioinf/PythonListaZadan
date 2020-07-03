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
args.pop(0) # nazwa własnego pliku
if '--decode' in args:
    args.pop(args.index('--decode'))
    if len(args) > 0:
        with open(args[0], "r") as plik:
            tekst = plik.read()
            print("Tekst rozszyfrowany: " + rozszyfruj(tekst))
    else:
        print("Podaj plik do rozsyzfrowania")
else:
    if len(args) > 0:
        with open(args[0], "r") as plik:
            tekst = plik.read()
            print("Tekst zaszyfrowany: " + szyfruj(tekst))
    else:
        print("Podaj plik do zasyzfrowania")
    