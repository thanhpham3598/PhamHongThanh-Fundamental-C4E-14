from turtle import *

def draw_star(x, y, length):
    penup()
    setpos(x, y)
    pendown()
    color('red')
    for i in range(5):
        forward(length)
        right(144)

# draw_star(30,70, 50)

speed(0)
color('blue')
for i in range(100):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(3, 10)
    draw_star(x, y, length)

    
mainloop()
