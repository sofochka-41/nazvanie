import random
def f(x):
    return x**2 + 2*x + 1

lower_limit = 0
upper_limit = 2   

summ = 0
for i in range(100000):
    x = lower_limit + (upper_limit - lower_limit) * random.random()
    summ += f(x)

integral = summ * (upper_limit - lower_limit) / 100000
print("Ответ:", integral)