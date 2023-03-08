from math import sqrt, atan, pi, sin, cos

class ComplexNum(object):
    re, im = 0, 0
    r, arg = 0, 0

    def __init__(self, re, im):
        self.re = re
        self.im = im
        self.r = sqrt(re**2 + im**2)
        if re > 0:
            self.arg = atan(self.im/self.re)
        elif re != 0:
            self.arg = pi + atan(self.im/self.re)

    def __eq__(self, other):
        return self.re == other.re and self.im == other.im
    def __str__(self):
        return f'{self.re} + {self.im}*i'
    def __add__(self, other):
        return ComplexNum(self.re + other.re, self.im + other.im)
    def __sub__(self, other):
        return ComplexNum(self.re - other.re, self.im - other.im)
    def __mul__(self, other):
        a, b, c, d = self.re, self.im, other.re, other.im
        return ComplexNum(a*c-b*d, a*d+b*c)
    
    # сопряжение комплексного числа
    def ComplСonjugate(self):
        return ComplexNum(self.re, -1*self.im)
    
    # взятие модуля комплексного числа
    def module(self):
        return sqrt(self.re**2 + self.im**2)
    
    # обратный элемент в поле
    def InverseNum(self):
        a, b = self.re, self.im
        return ComplexNum(a/(a**2 + b**2), (-b)/(a**2 + b**2))
    
    # тригонометрическая форма записи
    def TrigForm(self):
        return f'{self.r}(cos({self.arg}) + sin({self.arg})*i)'
    
    # возведение в степень комплексного числа по формуле Муавра
    def involution(self, n):
        res = ComplexNum(0, 0)
        res.r = (self.r)**n
        res.arg = self.arg * n
        res.re = res.r * cos(res.arg)
        res.im = res.r * sin(res.arg)
        return res

a = ComplexNum(1,1)
b = ComplexNum(2,1)
print(b.ComplСonjugate())
print(b.TrigForm())
print()
print(b.involution(5))