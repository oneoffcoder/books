import turtle

def up():
    t.setheading(90)
    t.forward(50)
    state = 'up'
    print(state)

def down():
    t.setheading(270)
    t.forward(50)
    state = 'down'
    print(state)
    

def right():
    t.setheading(0)
    t.forward(50)
    state = 'right'
    print(state)

def left():
    t.setheading(180)
    t.forward(50)
    state = 'left'
    print(state)

def toggle_pen_up_down():
    if t.isdown():
        t.penup()
        print('pen up')
    else:
        t.pendown()
        print('pen down')

def close():
    print('close')
    turtle.bye()

w = turtle.Screen()
w.title('Event Listening')

t = turtle.Turtle()
p_state = 'down'

w.onkey(up, 'Up')
w.onkey(down, 'Down')
w.onkey(right, 'Right')
w.onkey(left, 'Left')
w.onkey(close, 'q')
w.onkey(toggle_pen_up_down, 'p')

w.listen()

turtle.done()
