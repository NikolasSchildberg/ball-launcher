import turtle

# preset
t = 0
turtle.width(4)
turtle.setworldcoordinates(-50,-10,400,400)

# kinematics: parameters setting for parabolic motion
time_step = 0.2
x_0 = 0
v_x = 20
y_0 = 0
v_y0 = 80
a = -10

# setting turtle and backgorund appearence
turtle.bgcolor("#87cefa")
turtle.shape("circle")
turtle.fillcolor("yellow")

# kinematics: parabolic motion
def x(t):
    return  x_0 + v_x*t
def y(t):
    return  y_0 + v_y0*t + (a/2)*(t**2)

# moving and drawing
while(y(t)>=y_0):
    turtle.goto(x(t),y(t))
    t += time_step
    
    # dashing the line
    if(round(2*t) % 2 == 0):
        turtle.penup()
    if(round(2*t) % 2 == 1):
        turtle.pendown()
turtle.done()