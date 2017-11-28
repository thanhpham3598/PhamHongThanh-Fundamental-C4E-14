colors = ['red', 'blue', 'brown', 'yellow', 'grey']

from turtle import *

for i in range(5):
    color(colors[i])
    begin_fill()
    for a in range(2):
        forward(50)
        right(90)
        forward(100)
        right(90)
    end_fill()
    forward(50)

mainloop()
