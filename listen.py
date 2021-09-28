from turtle import Turtle, Screen

lizzy = Turtle()
lizzy.shape("turtle")
lizzy.color("cyan")
lizzy.forward(100)

screen = Screen()


def move_forward():
    lizzy.forward(20)

def move_backward():
    lizzy.backward(10)

def turn_right():
    new_heading = lizzy.heading() - 10
    lizzy.setheading(new_heading)

def turn_left():
    new_heading = lizzy.heading() + 10
    lizzy.setheading(new_heading)

def clear():
    lizzy.clear()
    lizzy.penup()
    lizzy.home()


screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_right, "a")
screen.onkey(turn_left, "d")
screen.onkey(clear, "c")


screen.exitonclick()
