import numpy
from numpy import array
from numpy.linalg import norm
from numpy.linalg import solve as solve_out_of_the_box

def gauss(a, b):
    a = a.copy()
    b = b.copy()

    def forward():
        # do something to a and b
        for k in range(len(b)-1):
            for i in range(k+1,len(b)):
                t = a[i][k]/a[k][k]
                b[i] = b[i] - (b[k] * t)
                
                for j in range(len(b)):
                    a[i][j] = a[i][j] - (a[k][j] * t)  
        

    def backward():
        x = numpy.zeros(len(b), dtype=float)
        # then do something to a and b
        x[len(b)-1] = b[len(b)-1]/a[len(b)-1][len(b)-1]
        for i in range(2,-1,-1):
            sum = 0
            for j in range(i+1, len(b)):
                sum += a[i][j]*x[j]
            x[i] = (b[i]-sum)/a[i][i]
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
