import turtle
laki = turtle.Turtle()
laki.shape('turtle')
laki.speed(1000000)
for i in range(20):
    for j in range(20):
        laki.forward(45)
        laki.left(30)
    laki.forward(50)
    laki.right(40)
