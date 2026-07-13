#Name(s):
#Final Project - Build Something Worth Showing Off
'''
This is the big one. At the end of camp you will demo this project at the
SHOWCASE, and it should be good enough to put on a resume or mention in a
college application. That means it is not just "code that works." It is a
project you designed, built, polished, and can explain.

WHAT MAKES IT SHOWCASE-WORTHY (the autograder checks for these):
  1. ORGANIZED: your code is split into clear, purposeful segments (functions optional), not one
     giant blob. (Aim for at least 3-4 functions with real jobs.)
  2. SUBSTANTIAL: this is a multi-day build, bigger than the mini-project.
  3. REAL LOGIC: decisions (if/elif/else) and repetition (loops) working together.
  4. DOCUMENTED: fill out PROJECT.md so a stranger (or a college admissions
     reader!) can understand what you built and how to run it.

Whether it is impressive, creative, and demo-ready is judged by humans at
showcase, not by the autograder.

============================= PICK YOUR TRACK =================================

TRACK A: IMAGE PROCESSING PROGRAM
  Build a program that opens an image and transforms it with a special
  function you write yourself: brightness adjustment, a color filter overlay,
  grayscale, mirror, pixelate, or invent your own effect.
  The Pillow library is preinstalled. The core moves:

      from PIL import Image
      img = Image.open("photo.png")
      width, height = img.size
      pixel = img.getpixel((x, y))          # (red, green, blue), each 0-255
      img.putpixel((x, y), (r, g, b))       # set a pixel
      img.save("output.png")                # then click it in VS Code to view!

  Brightness is a for loop over every pixel that multiplies r, g, b by a
  factor the user chooses (careful: values must stay between 0 and 255).
  A filter overlay nudges every pixel toward a color (add red, drop blue...).
  Level up: ask the user which effect to apply with input(), show a menu,
  process any image file they name, draw the result with turtle or pygame.

TRACK B: ADVENTURE GAME
  Build a text adventure where the player explores, makes choices, and wins
  or loses based on decisions and luck. Use random for surprises: treasure,
  traps, enemy encounters, dice rolls, critical hits.
  The shape of it: one function per location or scene, input() for choices,
  an inventory list, health or gold as numbers, and random.randint() for
  the unexpected. Level up: turn-based combat, a map, multiple endings,
  ASCII art title screens, a save-your-score high score.

TRACK C: YOUR OWN IDEA
  A bigger game (pygame or turtle), a quiz app, a tool that solves a real
  problem you have, a simulation, generative turtle art... Pitch it to your
  instructor FIRST, then build it. The four requirements above still apply.

=============================== PLAN FIRST ====================================
Before you write code, fill this in (it will keep you honest all week):

  MY PROJECT: (one sentence)
  THE PIECES I NEED TO BUILD: (list 3-6 functions or parts)
  WHAT I WILL DEMO AT SHOWCASE: (the 60-second version)

==============================================================================
Build your project below (and split it into more .py files if it gets big;
the grader reads all of them). Delete this line and start!
'''


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
# while score_a or score_b < 7:
#     for





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
        pen.write("Player B Wins!",
                align = "center",
                font=("Courier", 30, "normal"))
        break

    if score_a >= 10:
        pen.goto(0, 0)
        pen.write("Player A Wins!",
              align="center",
              font=("Courier", 30, "normal"))
        break
        


turtle.done()
