import random
import math

def Primality(n):
    if n == 2:
        return True
    if (n % 2 == 0):
        return False

    s = 0
    q = n - 1

    while q % 2 == 0:
        q >>= 1
        s += 1

    def check(a, q, n, s):
        x = a ** q % n
        if x == 1:
            return True
        for i in range(s-1):
            if x == n-1:
                return True
            x = x ** 2 % n
        return x == n-1

    for k in range(10):
        a = random.randint(2, n)
        if not check(a, q, n, s):
            return False
    return True

n = random.randint(1, 100000)
print(n,Primality(n))
