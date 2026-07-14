

While True:
        import turtle
        import time
        import random

# ---------------- Window Setup ----------------

        win = turtle.Screen()
        win.title("Pong by Python")
        win.bgcolor("blue")
        win.setup(width=800, height=600)
        win.tracer(0)


# ---------------- Game Variables ----------------

        score_a = 0
        score_b = 0
        game_over = False


# ---------------- Drawing Border ----------------

        border = turtle.Turtle()
        border.speed(0)
        border.color("white")
        border.penup()
        border.goto(-390, 290)
        border.pendown()

        for _ in range(2):
            border.forward(780)
            border.right(90)
            border.forward(580)
            border.right(90)

        border.hideturtle()


# ---------------- Center Line ----------------

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


# ---------------- Paddle A ----------------

        paddle_a = turtle.Turtle()
        paddle_a.speed(0)
        paddle_a.shape("square")
        paddle_a.color("red")
        paddle_a.shapesize(stretch_wid=5, stretch_len=1)
        paddle_a.penup()
        paddle_a.goto(-350, 0)


# ---------------- Paddle B ----------------

        paddle_b = turtle.Turtle()
        paddle_b.speed(0)
        paddle_b.shape("square")
        paddle_b.color("green")
        paddle_b.shapesize(stretch_wid=5, stretch_len=1)
        paddle_b.penup()
        paddle_b.goto(350, 0)


# ---------------- Ball ----------------

        ball = turtle.Turtle()
        ball.speed(0)
        ball.shape("circle")
        ball.color("white")
        ball.penup()
        ball.goto(0, 0)

        ball.dx = 0.6
        ball.dy = 0.6


# ---------------- Score Display ----------------

        pen = turtle.Turtle()
        pen.speed(0)
        pen.color("white")
        pen.penup()
        pen.hideturtle()
        pen.goto(0, 260)

        def update_score():
            pen.clear()
            pen.goto(0, 260)
            pen.write(
                f"Player A: {score_a}  Player B: {score_b}",
                align="center",
                font=("Courier", 24, "normal")
            )

        update_score()





        def paddle_a_up():
            if not game_over:
                y = paddle_a.ycor()
                if y < 240:
                    paddle_a.sety(y + 20)


        def paddle_a_down():
            if not game_over:
                y = paddle_a.ycor()
                if y > -240:
                    paddle_a.sety(y - 20)


        def paddle_a_right():
            if not game_over:
                x = paddle_a.xcor()
                if x < -50:
                    paddle_a.setx(x + 20)


        def paddle_a_left():
            if not game_over:
                x = paddle_a.xcor()
                if x > -350:
                    paddle_a.setx(x - 20)



        def paddle_b_up():
            if not game_over:
                y = paddle_b.ycor()
                if y < 240:
                    paddle_b.sety(y + 20)


        def paddle_b_down():
            if not game_over:
                y = paddle_b.ycor()
                if y > -240:
                    paddle_b.sety(y - 20)


        def paddle_b_right():
            if not game_over:
                x = paddle_b.xcor()
                if x < 350:
                    paddle_b.setx(x + 20)


        def paddle_b_left():
            if not game_over:
                x = paddle_b.xcor()
                if x > 50:
                    paddle_b.setx(x - 20)





            # Reset paddles
            paddle_a.goto(-350, 0)
            paddle_b.goto(350, 0)

            # Reset ball
            ball.goto(0, 0)
            ball.dx = random.choice([-1, 1])
            ball.dy = random.choice([-1, 1])

            # Reset text
            update_score()

            pen.clear()
            update_score()









        # ---------------- Keyboard Controls ----------------

        win.listen()

        # Player A controls
        win.onkeypress(paddle_a_up, "w")
        win.onkeypress(paddle_a_down, "s")
        win.onkeypress(paddle_a_left, "a")
        win.onkeypress(paddle_a_right, "d")

        # Player B controls
        win.onkeypress(paddle_b_up, "i")
        win.onkeypress(paddle_b_down, "k")
        win.onkeypress(paddle_b_left, "j")
        win.onkeypress(paddle_b_right, "l")


        win.onkeypress(reset_game, "r")


        while True:
            win.update()

            
            if game_over:
                time.sleep(0.01)
                continue


            
            ball.setx(ball.xcor() + ball.dx)
            ball.sety(ball.ycor() + ball.dy)


            

            if ball.ycor() > 280:
                ball.sety(280)
                ball.dy *= -1

            if ball.ycor() < -280:
                ball.sety(-280)
                ball.dy *= -1



            

            if ball.xcor() > 390:
                score_a += 1
                update_score()

                ball.goto(0, 0)
                ball.dx = random.choice([-1, 1])
                ball.dy = random.choice([-1, 1])


            if ball.xcor() < -390:
                score_b += 1
                update_score()

                ball.goto(0, 0)
                ball.dx = random.choice([-1, 1])
                ball.dy = random.choice([-1, 1])



            # ---------------- Paddle Collision ----------------

            # Right paddle
            if (330 < ball.xcor() < 350 and
                paddle_b.ycor() - 75 < ball.ycor() < paddle_b.ycor() + 75):

                ball.setx(330)
                ball.dx *= -1

                # Speed increase
                ball.dx *= 1.05
                ball.dy *= 1.05



            # Left paddle
            if (-350 < ball.xcor() < -330 and
                paddle_a.ycor() - 75 < ball.ycor() < paddle_a.ycor() + 75):

                ball.setx(-330)
                ball.dx *= -1

                # Speed increase
                ball.dx *= 1.05
                ball.dy *= 1.05



            # ---------------- Win Condition ----------------

            if score_a >= 10:
                game_over = True

                pen.clear()
                pen.goto(0, 40)
                pen.write(
                    "PLAYER A WINS!",
                    align="center",
                    font=("Courier", 30, "bold")
                )

                pen.goto(0, -20)
                pen.write(
                    "Click Restart or Press R",
                    align="center",
                    font=("Courier", 20, "normal")
                )


            if score_b >= 10:
                game_over = True

                pen.clear()
                pen.goto(0, 40)
                pen.write(
                    "PLAYER B WINS!",
                    align="center",
                    font=("Courier", 30, "bold")
                )

                pen.goto(0, -20)
                pen.write(
                    "Click Restart or Press R",
                    align="center",
                    font=("Courier", 20, "normal")
                )



            time.sleep(0.001)



            turtle.done()