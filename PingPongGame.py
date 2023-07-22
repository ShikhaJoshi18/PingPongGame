import turtle

window = turtle.Screen()  # it assigns an empty window to our variable
window.title("Ping Pong")  # giving title to our window
window.bgcolor("black")  # giving color to our window
window.setup(width=800, height=600)  # giving dimensions to our window(pixels)
window.tracer(0)

# score
score_a = 0
score_b = 0

# paddle left

Paddle_L = turtle.Turtle()  # creates object of type Turtle(class name)
Paddle_L.speed(0)  # used to change the speed of the turtle by the value of the argument it takes
Paddle_L.shape("square")  # to give shape to the paddle
Paddle_L.color("blue")
Paddle_L.penup()
Paddle_L.goto(-350, 0)
Paddle_L.shapesize(stretch_wid=5, stretch_len=1)

# Paddle right

Paddle_R = turtle.Turtle()  # creates object of type Turtle(class name)
Paddle_R.speed(0)  # used to change the speed of the turtle by the value of the argument it takes
Paddle_R.shape("square")  # to give shape to the paddle
Paddle_R.color("yellow")
Paddle_R.penup()
Paddle_R.goto(350, 0)
Paddle_R.shapesize(stretch_wid=5, stretch_len=1)

# ball

ball = turtle.Turtle()  # creates object of type Turtle(class name)
ball.speed(0)  # used to change the speed of the turtle by the value of the argument it takes
ball.shape("circle")  # to give shape to the paddle
ball.color("white")
ball.penup()
ball.dx = 0.07
ball.dy = -0.07

# pen

Pen = turtle.Turtle()
Pen.speed(0)  # 0 corresponds to max speed in turtle graphics
Pen.color("red")
Pen.penup()  # so that it does not draw a line while moving otherwise it'll leave lines behind it as it moves
Pen.hideturtle()
Pen.goto(0, 260)
Pen.write("Player A: 0 , Player B: 0", align="center", font=("courier", 24, "normal"))


# Moving the paddle

def Paddle_L_Up():
    y = Paddle_L.ycor() + 20
    if y + 50 <= 300:  # Limiting the paddle motion so it stays within the canvas
        Paddle_L.sety(y)


def Paddle_L_Down():
    y = Paddle_L.ycor() - 20  # to get the y coordinate of the left paddle
    if y - 50 >= -300:
        Paddle_L.sety(y)


def Paddle_R_Up():
    y = Paddle_R.ycor() + 20
    if y + 50 <= 300:  # Limiting the paddle motion so it stays within the canvas
        Paddle_R.sety(y)


def Paddle_R_Down():
    y = Paddle_R.ycor() - 20
    if y - 50 >= -300:
        Paddle_R.sety(y)


# keyboard binding
window.listen()
window.onkeypress(Paddle_L_Up,
                  "w")  # when the second argument key is pressed then the function of first argumwnt is called
window.onkeypress(Paddle_L_Down, "s")
window.onkeypress(Paddle_R_Up, "Up")
window.onkeypress(Paddle_R_Down, "Down")

while True:
    window.update()
    newx = ball.xcor() + ball.dx
    newy = ball.ycor() + ball.dy
    ball.setx(newx)
    ball.sety(newy)
    # border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy = ball.dy * -1
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy = ball.dy * -1
    if ball.xcor() > 390:
        score_a += 1
        Pen.clear()
        Pen.write("Player A: {} , Player B: {}".format(score_a, score_b), align="center",
                  font=("courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx = ball.dx * -1
    elif ball.xcor() < -390:
        score_b += 1
        Pen.clear()
        Pen.write("Player A: {} , Player B: {}".format(score_a, score_b), align="center",
                  font=("courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx = ball.dx * -1
    if (-350 < ball.xcor() < -340) and ball.ycor() < Paddle_L.ycor() + 50 and ball.ycor() > Paddle_L.ycor() - 50:
        ball.dx = ball.dx * -1  # reversing it's direction
    if (350 > ball.xcor() > 340) and ball.ycor() < Paddle_R.ycor() + 50 and ball.ycor() > Paddle_R.ycor() - 50:
        ball.dx = ball.dx * -1  # reversing it's direction
















