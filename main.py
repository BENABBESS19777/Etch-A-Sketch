from turtle import Turtle, Screen

tim = Turtle()
# Set up screen ===============================
screen = Screen()
screen.bgcolor("white")
screen.title("Etch-A-Sketch")
screen.setup(width = 600, height = 400)


def move_forwards():
    tim.forward(10)
    
def move_backwards():
    tim.backward(10) 
    
def move_counter_clockwise():
    tim.left(5) 
    
def move_clockwise():
    tim.left(-5) 
    
def clear_drawing():
    tim.clear() 
    tim.penup()  
    tim.home()
    tim.pendown()         


screen.listen()
screen.onkey(key="W", fun=move_forwards)
screen.onkey(key="S", fun=move_backwards)
screen.onkey(key="A", fun=move_counter_clockwise)
screen.onkey(key="D", fun=move_clockwise)
screen.onkey(key="C", fun=clear_drawing)
screen.exitonclick()
