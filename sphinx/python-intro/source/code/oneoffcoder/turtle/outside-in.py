import turtle

def spiral(size, t, delta=-5):
    for i in range(4):
        t.fd(size)
        t.left(90)
        size = size + delta

w = turtle.Screen()
w.title('Outside In')

t = turtle.Turtle()

t.color('blue')
nums = list(range(26, 147, 20))
nums.reverse()

for num in nums:
    spiral(num, t)

turtle.done()