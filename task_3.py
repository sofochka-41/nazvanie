import turtle as tl

def fract(len):
    if len >=20:
        tl.forward(len)
        tl.right(60)
        fract(len / 2)
        tl.left(60)
        fract(len / 2)
        tl.right(120)
        fract(len / 2)
        tl.left(120)
        fract(len / 2)
        tl.right(240)
        fract(len / 2)
        tl.left(240)
        fract(len / 2)
        tl.right(300)
        fract(len / 2)
        tl.left(300)
        fract(len / 2)
        tl.backward(len)
        

        
        
        

len = 200
tl.delay(0)  # уменьшение задержки для скорости
tl.penup()
tl.goto(0, -len * 2)
tl.setheading(90)
tl.pendown()

fract(len)
tl.done()