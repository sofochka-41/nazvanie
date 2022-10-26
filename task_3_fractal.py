import turtle as tl  # Подключение модуля Черепашка для рисования. Для сокращения называем 'turtle' 'tl'

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple' ]  # Список цветов, которые мы будем использовать в последствии

def fract(len):  # Функция, которая будет рисовать большие треугольники, а внутни них маленькие
    if len >=20:  # len - длинна линии; устанавливаем минимальную длину линии, чтобы функция остановилась.
        for i in range(3):  # цикл рисует треугольник; т.к. у треугольника 3 стороны нам надо 3 раза повернуть черепашку и трижды нарисовать прямую 
            tl.right(120)  # Поворачиваем черепашку на 120; т.к. 360 / 3 = 120
            tl.forward(len)  # Рисуем прямую длины len
        fract(len / 2)  # Вызываем программу для уменьшенной в 2 раза len, чтобы написовать маленькие треугольники

len = 400  # пусть начальная длина стороны будет 400 пикселей

tl.delay(0)  # Уменьшение задержки для скорости
tl.shape("turtle")  # Заменяем стрелочку, которая рисует, на черепашку
for h in range(6):  # Чтобы получился шестиугольник из треугольников нарисуем 6 треугольников
    tl.color(colors[h])  # Каждый новый большой треугольник будет нового цвета из списка colors
    tl.right(60)  # Чтобы не рисовать треугольники на одном месте повернём черепашку
    for t in range(3):  # Чтобы в каждой вершине большого треугольника был треугольник поменьше надо запустить функцию трижды
        tl.right(60)  # Разворачиваем черепашку, чтобы трижды не рисовать на одном месте 
        tl.forward(len)  # Чертим прямую, чтобы большой треугольник остался на месте, но переместились поменьше в вершинах
        fract(len)  # Вызываем функцию, чтобы написовать большой треугольник
        tl.right(60)  # Разворачиваем черепашку, чтобы большой треугольник остался на месте
tl.done()  # Предотвращает закрытие холста