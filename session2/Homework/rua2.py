from turtle import *

n = 2
for a in range(4):
    n = int(n + 1)
    if a % 2 == 0:
        color("blue")
    else:
        color("red")
    for b in range(n):
        forward(50)
        left(360/n)
mainloop()
