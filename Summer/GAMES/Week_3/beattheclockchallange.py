import turtle
import random
import time

# --- Screen setup ---
wn = turtle.Screen()
wn.title("⏳ Beat the Clock Challenge")
wn.bgcolor("lightyellow")
wn.setup(width=800, height=600)
wn.tracer(0)  # Turn off automatic animation for smoother control

# --- Game Variables ---
score = 0              # Player's score
time_left = 15         # Countdown timer in seconds
game_over = False      # Game state flag

# --- Player setup ---
player = turtle.Turtle()
player.shape("turtle")
player.color("blue")
player.penup()
player.speed(0)
player.goto(0, 0)

# --- Target setup (object to collect for points) ---
target = turtle.Turtle()
target.shape("circle")
target.color("red")
target.penup()
target.speed(0)
target.goto(random.randint(-350, 350), random.randint(-250, 250))

# --- Pen for writing score & time ---
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.goto(0, 260)

def update_score_time():
    """Updates the scoreboard at the top."""
    pen.clear()
    pen.write(f"Score: {score}   Time Left: {time_left}s",
              align="center", font=("Arial", 18, "bold"))

update_score_time()

# --- Player movement functions ---
def move_up():
    y = player.ycor() + 20
    if y < 290:
        player.sety(y)

def move_down():
    y = player.ycor() - 20
    if y > -290:
        player.sety(y)

def move_left():
    x = player.xcor() - 20
    if x > -390:
        player.setx(x)

def move_right():
    x = player.xcor() + 20
    if x < 390:
        player.setx(x)

# --- Keyboard bindings ---
wn.listen()
wn.onkeypress(move_up, "Up")
wn.onkeypress(move_down, "Down")
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")

# --- Countdown Timer Function ---
def countdown():
    """Reduces the time left every second until game over."""
    global time_left, game_over
    if time_left > 0:
        time_left -= 1
        update_score_time()
        wn.ontimer(countdown, 1000)  # Call this function again after 1 second
    else:
        game_over = True
        show_game_over()

# --- Game Over Display ---
def show_game_over():
    """Displays a game over message in the center."""
    pen.goto(0, 0)
    pen.write(f"⏰ Time's Up! Final Score: {score}",
              align="center", font=("Arial", 24, "bold"))

# --- Start Countdown ---
countdown()

# --- Main Game Loop ---
while not game_over:
    wn.update()

    # Check if player touches target
    if player.distance(target) < 20:
        score += 1  # Increase score
        update_score_time()
        # Move target to new random position
        target.goto(random.randint(-350, 350), random.randint(-250, 250))

wn.mainloop()
