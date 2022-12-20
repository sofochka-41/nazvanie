import random;
import math

def my_gcd(a,b):
    if b == 0:
        return a
    else:
        return my_gcd(b, a % b)

a = random.randint(1, 1000)
b = random.randint(1, 1000)
print(a,b)
if (math.gcd(a,b) == my_gcd(a,b)):
    print(f'gcd({a},{b})=',my_gcd(a,b))
else:
    print('Ошибка в вычислениях')
