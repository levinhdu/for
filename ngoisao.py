import turtle

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Star")

t = turtle.Turtle()
t.speed(0)
t.color("#FF0000")

for j in range (1,100):
    for i in range (1,6):
        t.left(144)
        t.forward(200)
    t.left(5)

turtle.done()