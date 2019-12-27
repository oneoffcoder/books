import turtle

t = turtle.Turtle()

dot_distance = 25
width = 5
height = 7

shapes = ['arrow', 'circle', 'classic', 'square', 'triangle', 'turtle']

t.penup()

for y in range(height):
    shape = shapes[y % len(shapes)]
    
    t.shape(shape)

    for i in range(width):
        t.dot()
        t.forward(dot_distance)
    t.backward(dot_distance * width)
    t.right(90)
    t.forward(dot_distance)
    t.left(90)
    
turtle.done()