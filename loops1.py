from turtle import *
# for loop ko likhne ka tareeka 
speed('fastest')
pencolor('blue')
pensize(5)

for i in range(8,0,-1):
    fd(120)
    rt(45)
    write (f'n={i}', font=("Calibri",16))
hideturtle()
mainloop()