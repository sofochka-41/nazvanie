import random
import math

def egcd(a,b):
    if b ==0:
        return (1, 0, a)
    else:
        (x,y,d) = egcd(b, a % b)
        return (y, x-(a//b)*y,d)

a = random.randint(1,1000)
b = random.randint(1,1000)
x,y,d = egcd(a,b)
if (a*x+b*y == d) and (math.gcd(a,b) == d):
    print(f'Алгоритм работает a={a}, b={b}, x={x}, y={y}, gcd({a},{b})={d}')
else:
    print('Ошибка в вычислениях')
