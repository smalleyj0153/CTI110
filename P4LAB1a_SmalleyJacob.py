import turtle
wn = turtle.Screen()
jake = turtle.Turtle()

for _ in range(4):
    jake.forward(100)
    jake.left(90)

jake.penup()
jake.forward(150)
jake.pendown()

for _ in range(3):
    jake.forward(100)
    jake.left(120)
