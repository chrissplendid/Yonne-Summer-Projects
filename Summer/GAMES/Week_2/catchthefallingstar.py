import turtle
import random
import winsound  # For sound effects on Windows

# --- Setup the screen ---
wn = turtle.Screen()
wn.title("⭐ Catch the Falling Star ⭐")
wn.bgcolor("black")
wn.setup(width=700, height=700)
wn.tracer(0)  # Turn off automatic screen updates

# --- Score variable ---
score = 0

# --- Draw the catcher (player) ---
player = turtle.Turtle()
player.shape("square")
player.color("white")
player.shapesize(stretch_wid=1, stretch_len=5)  # Paddle-like shape
player.penup()
player.goto(0, -250)

# --- Draw the star ---
star = turtle.Turtle()
star.shape("turtle")
star.color("yellow")
star.penup()
star.goto(random.randint(-280, 280), 250)
star_speed = 0.1

# --- Draw the score display ---
pen = turtle.Turtle()
pen.hideturtle()
pen.color("white")
pen.penup()
pen.goto(0, 260)
pen.write(f"Score: {score}", align="center", font=("Arial", 17, "normal"))

# --- Player movement ---
def move_left():
    x = player.xcor()
    x -= 20
    if x < -280:
        x = -280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += 20
    if x > 280:
        x = 280
    player.setx(x)

# --- Keyboard bindings ---
wn.listen()
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")

# --- Main game loop ---
while True:
    wn.update()

    # Move the star down
    star.sety(star.ycor() - star_speed)

    # Check if star is caught
    if star.ycor() < -230 and abs(player.xcor() - star.xcor()) < 50:
        score += 1
        winsound.Beep(800, 100)  # Catch sound
        star.goto(random.randint(-280, 280), 250)
        pen.clear()
        pen.write(f"Score: {score}", align="center", font=("Arial", 18, "normal"))

    # Check if star missed
    if star.ycor() < -280:
        winsound.Beep(400, 200)  # Miss sound
        star.goto(random.randint(-280, 280), 250)
