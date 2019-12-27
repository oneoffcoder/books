import turtle 

t = turtle.Turtle()

colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
speed = 10

for i in range(180):
    color = colors[i % 6]

    t.pencolor(color)
    t.speed(speed)

    t.forward(100)
    t.right(30)
    t.forward(20)
    t.left(60)
    t.forward(50)
    t.right(30)
    
    t.penup()
    t.setposition(0, 0)
    t.pendown()
    
    t.right(2)

    speed = speed + 2
    
turtle.done()