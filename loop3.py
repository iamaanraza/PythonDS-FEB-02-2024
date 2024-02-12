from turtle import *

pencolor('yellow')
bgcolor('black')

for i in range(5): # nest loop ke andar kitne bhi loops laga sakte hain
    fd(100)
    for i in range(5):
        fd(75)
        lt(360/5)
    lt(360/5)
    dot(10)

    
    

hideturtle()
mainloop()        