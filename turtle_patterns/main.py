import turtle 
t=turtle.Turtle()
screen=turtle.Screen()
screen.title("flower design...")
screen.bgcolor('#db6bb0')
t.shape('turtle')
t.pencolor('red')
t.pensize(2)
t.speed(1)
t.fillcolor('green')
t.begin_fill()
for i in range(10):
    
    t.circle(100)
    t.left(40)
t.end_fill()



