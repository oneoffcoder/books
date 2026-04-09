import turtle

def spiral(size, t, delta=-5):
    for i in range(4):
        t.fd(size)
        t.left(90)
        size = size + delta

w = turtle.Screen()
w.title('Inside Out')

t = turtle.Turtle()
t.color('red')
nums = list(range(6, 147, 20))

for num in nums:
    spiral(num, t, delta=5)

turtle.done()