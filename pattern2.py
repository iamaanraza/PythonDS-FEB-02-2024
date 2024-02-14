from turtle import*
speed(0)

def polygon(side,size,color): # required arguments .
    fillcolor(color)
    begin_fill()
    for _ in range(side):
        fd(size)
        lt(360/side)
    end_fill()

# testing the function

for _ in range(6):
    polygon(side =10, size=50, color='red') # named arguments 
    polygon(side =6, size= 20, color= 'green')
    polygon(4,100,color='yellow')
    lt(60)

hideturtle()
mainloop()    
