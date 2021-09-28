import turtle as turtle_module
import random

turtle_module.colormode(255)
lizzy = turtle_module.Turtle()
lizzy.speed("fastest")
lizzy.penup()
color_list = [(202, 164, 109), (233, 240, 245), (150, 75, 49), (223, 205, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19)]
lizzy.setheading(225)
lizzy.forward(300)
lizzy.setheading(0)
num_of_dots = 100

for dot_count in range(1, num_of_dots + 1):
    lizzy.dot(20, random.choice(color_list))
    lizzy.forward(50)

    if dot_count % 10 == 0:
        lizzy.setheading(90)
        lizzy.forward(50)
        lizzy.setheading(900)
        lizzy.forward(500)
        lizzy.setheading(0)


screen = turtle_module. Screen()
screen.exitonclick()

