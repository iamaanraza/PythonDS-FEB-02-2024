from turtle import *
# while loop to likne ka tareeka

speed('fastest')

s = 0 # define kara hai
while s < 250: # intitalize kiya hai
    fd(50 + s) # what to do
    lt(60)
    write(s)
    dot(10)
    s += 5 # after ever loop +5

hideturtle()
mainloop()