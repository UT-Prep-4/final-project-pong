import turtle
import time



# --- Window Setup ---
win = turtle.Screen()
win.title("Pong by Python")
win.bgcolor("blue")
win.setup(width=800, height=600)
win.tracer(0)

# --- Score Tracking ---
score_a = 0
score_b = 0
game_over = False







# --- Paddle A (Left) ---
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("red")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# --- Paddle B (Right) ---
paddle_b = turtle.Turtle()
paddle_b.speed(10)
paddle_b.shape("square")
paddle_b.color("green")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

line = turtle.Turtle()
line.speed(0)
line.color("white")
line.penup()
line.goto(0, 290)
line.setheading(270)

for _ in range(29):
    line.pendown()
    line.forward(10)
    line.penup()
    line.forward(10)

line.hideturtle()

# --- Ball ---
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
#SPEED OF DA BALL
ball.dx = 1.0
ball.dy = 1.0


# --- Pen (Score Display) ---
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# --- Movement Functions ---
def paddle_a_up():
    y = paddle_a.ycor()
    if y < 250: paddle_a.sety(y + 75)

def paddle_a_down():
    y = paddle_a.ycor()
    if y > -240: paddle_a.sety(y - 75)

def paddle_b_up():
    y = paddle_b.ycor()
    if y < 250: paddle_b.sety(y + 75)

def paddle_b_down():
    y = paddle_b.ycor()
    if y > -240: paddle_b.sety(y - 75)
def paddle_a_right():
    x = paddle_a.xcor()
    if x < -50: paddle_a.setx(x + 75)
def paddle_a_left():
    x = paddle_a.xcor()
    if x > -350: paddle_a.setx(x - 75)
def paddle_b_right():
    x = paddle_b.xcor()
    if x < 350: paddle_b.setx(x + 75)
def paddle_b_left():
    x = paddle_b.xcor()
    if x > 50: paddle_b.setx(x - 75)

def restart_game():
    global score_a 
    global score_b
    global game_over
    paddle_a.goto (-350,0)
    paddle_b.goto (350,0)
    ball.goto(0,0)
    ball.showturtle()
    
    score_a = 0
    score_b = 0
    game_over = False

    pen.clear()
    pen.goto(0, 260)
    pen.write(
        "Player A: 0  Player B: 0",
        align="center",
        font=("Courier", 24, "normal")

# --- Keyboard Bindings ---
win.listen()
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "s")
win.onkeypress(paddle_b_up, "i")
win.onkeypress(paddle_b_down, "k")
win.onkeypress(paddle_a_right, "d")
win.onkeypress(paddle_a_left, "a")
win.onkeypress(paddle_b_right, "l")
win.onkeypress(paddle_b_left, "j")
win.onkeypress(restart_game, "r")


# --- Main Game Loop ---
while True:
    win.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    

    

    # Top/Bottom boundary collision
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.dy *= -1

    # Right/Left boundary (Scoring)
    if ball.xcor() > 390:
        score_a += 1
        ball.goto(0, 0)
        ball.dx *= -1
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}",
            align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        score_b += 1
        ball.goto(0, 0)
        ball.dx *= -1
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}",
              align="center", font=("Courier", 24, "normal"))


    # Paddle collision


    if (paddle_b.xcor()-10 < ball.xcor() and ball.xcor() < paddle_b.xcor() + 10) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50) or \
       (paddle_a.xcor()-10 < ball.xcor() and ball.xcor() < paddle_a.xcor() + 10) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.dx *= -1

   

        



    
        
    time.sleep(0.001)


    if score_b >= 10:
        pen.goto(0,0)
        game_over = True
        ball.hideturtle()
        pen.write("Player B Wins!",
                align = "center",
                font=("Courier", 30, "normal"))
        

    if score_a >= 10:
        pen.goto(0, 0)
        game_over = True
        ball.hideturtle()        
        pen.write("Player A Wins!",
              align="center",
              font=("Courier", 30, "normal"))
        
        


turtle.done()
