import turtle

w = turtle.Screen()
w.title('Hexagon')

t = turtle.Turtle()

n_sides = 6
s_len = 70
angle = 360.0 / n_sides

for i in range(n_sides):
    t.forward(s_len)
    t.right(angle)

turtle.done()