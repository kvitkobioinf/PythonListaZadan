class RomanParse:
    def __init__(self, number):
        self.numbers = [(1000,'M'), (900, 'CM'), (500,'D'), (400, 'CD'), (100,'C'), (90, 'XC'), (50,'L'), (40, 'XL'), (10,'X'), (9, 'IX'), (5,'V'), (4, 'IV'), (1,'I')]
        
        if int == type(number):
            self.arabic = number
            self.roman = self.arabic_to_roman()
        else:
            self.roman = number
            self.arabic = self.roman_to_arabic()

    def roman_to_arabic(self):
        tot = 0
        for i in range(0, len(self.roman)):
            for each in self.numbers:
                if self.roman[i] == each[1]:
                    if each[0] > tot:
                        tot = each[0] - tot
                    else:
                        tot = tot + each[0]

        return tot

    def arabic_to_roman(self):
        arabic = self.arabic
        result = ''
        for denom, roman_digit in self.numbers:
            result += roman_digit * int((arabic / denom))
            arabic %= denom
        return result

if __name__ == "__main__":
    num1 = RomanParse("XCV")
    print(num1.roman, num1.arabic)
    num2 = RomanParse(2020)
    print(num2.roman, num2.arabic)