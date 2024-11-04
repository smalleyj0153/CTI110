#Jacob Smalley
#3 Nov 2024
#P4LAB1b
#My initials JS using turtle.

import turtle
wn = turtle.Screen()

t = turtle.Turtle()
t.speed(8)

for _ in range(1):
    # Draw the first part (line and arc)
    t.penup()
    t.goto(0, 100)
    t.pendown()
    t.forward(80)
    t.back(40)
    t.right(90)
    t.forward(200)
    t.right(90)
    t.circle(-50, 90)
# Reposition and draw the second part (S shape)
    t.penup()
    t.goto(140, 100)
    t.pendown()
    t.right(280)
    t.circle(50, 180)  # Top part of 'S'
    t.circle(-50, 180)  # Bottom part of 'S'
# Hide the turtle and finish
    t.hideturtle()
    turtle.done()

#Pseudocode
#Import turtle.
#Draw the letter J.
#Draw the letter S.
