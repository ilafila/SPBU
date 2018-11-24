# Посоветовался с Алексеем Ковгаром
class Roman:
    def __init__(self, num):
        if num > 1999:
            raise ValueError
        self.num = num
        self.rom_num = self.rom()

    def __str__(self):
        return self.rom_num

    def __eq__(self, other):
        return self.num == other.num

    def __int__(self):
        return self.num

    def __add__(self, other):
        return Roman(self.num + other.num)

    def __sub__(self, other):
        return Roman(self.num - other.num)

    def __mul__(self, other):
        return Roman(self.num * other.num)

    def __floordiv__(self, other):
        return Roman(self.num // other.num)

    def __mod__(self, other):
        return Roman(self.num % other.num)

    def rom(self):
        result = ''
        loc_num = self.num
        if loc_num >= 1000:
            result += 'M'
            loc_num -= 1000
        if loc_num >= 900:
            result += 'CM'
            loc_num -= 900
        if loc_num >= 500:
            result += 'D'
            loc_num -= 500
        if loc_num >= 400:
            result += 'CD'
            loc_num -= 400
        if loc_num >= 100:
            result += 'C' * (loc_num // 100)
            loc_num %= 100
        if loc_num >= 90:
            result += 'XC'
            loc_num -= 90
        if loc_num >= 50:
            result += 'L'
            loc_num -= 50
        if loc_num >= 40:
            result += 'XL'
            loc_num -= 40
        if loc_num >= 10:
            result += 'X' * (loc_num // 10)
            loc_num %= 10
        if loc_num >= 9:
            result += 'IX'
            loc_num -= 9
        if loc_num >= 5:
            result += 'V'
            loc_num -= 5
        if loc_num >= 4:
            result += 'IV'
            loc_num -= 4
        if loc_num >= 1:
            result += 'I' * (loc_num // 1)
        return result
