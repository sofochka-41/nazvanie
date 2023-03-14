import itertools 
from typeguard import typechecked

class Fib:    
    """По объектам этого класса можно итерироваться и получать чисела Фибоначчи"""

    class _Fib_iter:
        """Внутренний класс — итератор"""

        @typechecked
        def __init__(self) -> None:
            self.i = 0
            self.j = 1
        
        @typechecked 
        def __next__(self) -> int: 
            self.j = self.i + self.j
            self.i = self.j - self.i
            return self.j 

    @typechecked 
    def __iter__(self) -> '_Fib_iter':
        """Создать и вернуть итератор"""
        return Fib._Fib_iter()

fibb = Fib()
for f in fibb:
    print (f)
    if f>600:
        break
