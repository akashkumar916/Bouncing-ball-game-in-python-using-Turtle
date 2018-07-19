import turtle
import  random

var1=turtle.Screen()
var1.title('Boucing ball')
var1.bgcolor('black')
listball=[]
color=['red','yellow','blue','green','white','pink']
shape=['circle']
for i in range(5):
    listball.append(turtle.Turtle())

for ball in listball:

    ball.shape(random.choice(shape))
    ball.color(random.choice(color))

    ball.penup()


    x=random.randint(-280,280)
    ball.goto(x,200)


    ball.dx=1.5
    ball.dy=0
    v=random.randint(0,30)
    gravity=2
while True:
   for ball in listball:
    ball.dy-=gravity
    y=ball.ycor()
    ball.sety(y+ball.dy)
    ball.setx(ball.xcor() + ball.dx)



    if(ball.ycor()<-280):
        ball.rt(v)
        ball.dy*=-1
    if(ball.ycor()>200):
        ball.rt(v)
        ball.dy *= -1
    if(ball.xcor()<-300):
        ball.rt(v)
        ball.dx*=-1

    if (ball.xcor() >300):
        ball.rt(v)
        ball.dx *= -1

