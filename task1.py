import numpy
from numpy import array
from numpy.linalg import norm
from numpy.linalg import solve as solve_out_of_the_box

def gauss(a, b):
    a = a.copy()
    b = b.copy()

    def forward():
    # do something to a and b
        for i in range(len(a)):
            # Находим максимальный элемент в столбце
            max_el = abs(a[i][i])
            max_row = i
            for k in range(i + 1, len(a)):
                if abs(a[k][i]) > max_el:
                    max_el = abs(a[k][i])
                    max_row = k
            # Переставляем строки
            for k in range(i, len(a)):
                tmp = a[max_row][k]
                a[max_row][k] = a[i][k]
                a[i][k] = tmp
            tmp = b[max_row]
            b[max_row] = b[i]
            b[i] = tmp
            # Приводим к треугольному виду
            for k in range(i + 1, len(a)):
                c = -a[k][i] / a[i][i]
                for j in range(i, len(a)):
                    if i == j:
                        a[k][j] = 0
                    else:
                        a[k][j] += c * a[i][j]
                b[k] += c * b[i]

    def backward():
        x = numpy.zeros(len(b), dtype=float)
        # then do something to a and b
        for i in range(len(a) - 1, -1, -1):
            x[i] = b[i] / a[i][i]
            for k in range(i - 1, -1, -1):
                b[k] -= a[k][i] * x[i]
        return x

    forward()
    x = backward()
    return x

a = array([
    [1.5, 2.0, 1.5, 2.0],
    [3.0, 2.0, 4.0, 1.0],
    [1.0, 6.0, 0.0, 4  ],
    [2.0, 1.0, 4.0, 3  ]
], dtype=float)

b = array([5, 6, 7, 8], dtype=float)

oob_solution = solve_out_of_the_box(a, b)
solution = gauss(a, b)

print(solution)
print("Макс отклонение компоненты решения:", norm(solution-oob_solution, ord=1))
