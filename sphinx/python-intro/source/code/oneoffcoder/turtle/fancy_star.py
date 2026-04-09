import turtle

w = turtle.Screen()
w.title('Fancy Star')

t = turtle.Turtle()

for i in range(20):
    t.forward(i * 10)
    t.right(144)

turtle.done()