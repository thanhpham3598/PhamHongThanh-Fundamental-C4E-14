colors = ['red', 'blue', 'brown', 'yellow', 'grey']

from turtle import *

for i in range(5):
    color(colors[i])
    for a in range(i+3):
        forward(100)
        left(360/(i+3))
mainloop()
