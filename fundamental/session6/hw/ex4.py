from turtle import *
from ex3 import draw_square


for i in range(30):
    draw_square(i * 5, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()

mainloop()

# Bài này em ko import được :v, nhưng copy sang bài ex3 thì lại vẽ bình thường:)))
