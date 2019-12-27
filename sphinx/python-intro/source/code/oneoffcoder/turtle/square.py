import turtle

# w is an instance of Screen
# we choose w as the variable name to denote `window`
# we will use the terms `screen` and `window` interchangeably
w = turtle.Screen()

# let's set a title for the window
w.title('Square')

# t is an instance of Turtle
# a Turtle is also known as a `pen`
t = turtle.Turtle()

# we will loop 4 times
# each time, we make the turtle move forward and turn right 90 degrees
for i in range(4):
    t.forward(50)
    t.right(90)

# starts the event loop
# the event loop listens for events
turtle.done()