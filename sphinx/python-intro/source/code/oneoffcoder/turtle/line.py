import turtle

# w is an instance of Screen
# we choose w as the variable name to denote `window`
# we will use the terms `screen` and `window` interchangeably
w = turtle.Screen()

# let's set a title for the window
w.title('Line')

# t is an instance of Turtle
# a Turtle is also known as a `pen`
t = turtle.Turtle()

# draw a line
t.forward(50)

# starts the event loop
# the event loop listens for events
turtle.done()