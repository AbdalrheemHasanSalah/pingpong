import turtle

wind=turtle.Screen() #to show screen of the game 
wind.title("ping pong by Abdalrheem")#to give the title of window
wind.bgcolor("black")
wind.setup(width=800,height=600)
wind.tracer(0)#Turns turtle animation off and set delay for update drawings(prevent update the screen by it self ).




#madrab1
madrab1=turtle.Turtle()
madrab1.speed(0)#to give the speed of draw madrab1 to show in screen(0 to make no slow in drawing shape).
madrab1.shape("square")
madrab1.color("blue")
madrab1.shapesize(stretch_wid=5,stretch_len=1)#that mean set the width stretch_wid(20*5) and set the height stretch_len(20*1)
madrab1.penup()#no drawing when move.
madrab1.goto(-350,0)#to git the shape in screen 


#madrab2
madrab2=turtle.Turtle()
madrab2.speed(0)#to give the speed(animation) of draw madrab1 to show in screen(0 to make no slow in drawing shape).
madrab2.shape("square")
madrab2.color("red")
madrab2.shapesize(stretch_wid=5,stretch_len=1)#that mean set the width stretch_wid(20*5) and set the height stretch_len(20*1)
madrab2.penup()#no drawing when move.
madrab2.goto(350,0)#to git the shape position in screen 

#ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx=.25
ball.dy=.25

#score
score1=0
score2=0

score=turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0,260)
score.write("player 1 :0  player 2 : 0 ",align="center",font=("Courier",24,"normal"))
#functions 
def madrab1_Up():
    y=madrab1.ycor()#get y coordinate
    y+=20
    madrab1.sety(y)
def madrab1_down():
    y=madrab1.ycor()#get y coordinate
    y-=20
    madrab1.sety(y)#set y coordinate

def madrab2_Up():
    y=madrab2.ycor()#get y coordinate
    y+=20
    madrab2.sety(y)
def madrab2_down():
    y=madrab2.ycor()#get y coordinate
    y-=20
    madrab2.sety(y)    
#keyboard bindings
wind.listen()#tell the window to expect keyboard input 
wind.onkeypress(madrab1_Up,"w")
wind.onkeypress(madrab1_down,"s")
wind.onkeypress(madrab2_Up,"Up")
wind.onkeypress(madrab2_down,"Down")





#main game loop
while True:
    wind.update()#update the screen everytime loop run.

    #move the ball
    ball.setx(ball.xcor()+ball.dx)#ball start at 0 and every time loops run---->+2 xaxis
    ball.sety(ball.ycor()+ball.dy)#ball start at 0 and every time loops run---->+2 yaxis

    #border check 300px and ball 20px
    if ball.ycor()>290:#if ball reach border up
        ball.sety(290)
        ball.dy*=-1 
    #-300px and ball 20px    
    if ball.ycor()<-290:#if ball reach border down
        ball.sety(-290)
        ball.dy*=-1
    if ball.xcor()>390:#if ball reach right border
        ball.goto(0,0)
        score1+=1
        score.clear()
        score.write(f"player 1 :{score1}  player 2 :{score2} ",align="center",font=("Courier",24,"normal"))
        ball.dx *=-1 #reverse x direction
    if ball.xcor()<-390:
        ball.goto(0,0) 
        score2+=1 
        score.clear()
        score.write("player 1 :{}  player 2 :{} ".format(score1,score2),align="center",font=("Courier",24,"normal"))
        ball.dx *=-1

    #collision madrab and ball     
    if ball.xcor()>340 and ball.xcor()<350 and (ball.ycor()<madrab2.ycor()+40 and ball.ycor()>madrab2.ycor()-40):
        ball.setx(340)
        ball.dx*=-1
    if ball.xcor()<-340 and ball.xcor()>-350 and (ball.ycor()<madrab1.ycor()+40 and ball.ycor()>madrab1.ycor()-40):
        ball.setx(-340)
        ball.dx*=-1










