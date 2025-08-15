import turtle
import time

# --- Setup the screen ---
wn = turtle.Screen()
wn.title("🐢 Level Up Platformer")
wn.setup(width=800, height=600)
wn.tracer(0)

# --- Game variables ---
level = 1
gravity = -0.5
jump_strength = 10
is_jumping = False
y_velocity = 0

# --- Backdrop colors per level ---
backdrops = {
    1: "lightblue",
    2: "lightgreen",
    3: "orange"
}

# --- Player setup ---
player = turtle.Turtle()
player.shape("square")
player.color("blue")
player.shapesize(stretch_wid=1, stretch_len=1)
player.penup()
player.goto(-350, -250)

# --- Platform (goal) setup ---
goal = turtle.Turtle()
goal.shape("square")
goal.color("gold")
goal.shapesize(stretch_wid=1, stretch_len=3)
goal.penup()
goal.goto(300, -250)

# --- Level text display ---
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.color("black")
pen.goto(0, 260)

def draw_level_text():
    pen.clear()
    pen.write(f"Level {level}", align="center", font=("Arial", 20, "bold"))

# --- Controls ---
def move_left():
    x = player.xcor() - 20
    if x < -380:
        x = -380
    player.setx(x)

def move_right():
    x = player.xcor() + 20
    if x > 380:
        x = 380
    player.setx(x)

def jump():
    global is_jumping, y_velocity
    if not is_jumping:
        is_jumping = True
        y_velocity = jump_strength

wn.listen()
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")
wn.onkeypress(jump, "space")

# --- Function to load a level ---
def load_level(lvl):
    wn.bgcolor(backdrops.get(lvl, "gray"))
    player.goto(-350, -250)
    goal.goto(300, -250)
    draw_level_text()

# --- Load first level ---
load_level(level)

# --- Main game loop ---
while True:
    wn.update()

    # Apply gravity
    if is_jumping:
        new_y = player.ycor() + y_velocity
        y_velocity += gravity  # Gravity pulls down
        if new_y <= -250:  # Ground level
            new_y = -2
            is_jumping = False
            y_velocity = 0
        player.sety(new_y)

    # Check if player reaches goal
    if abs(player.xcor() - goal.xcor()) < 40 and abs(player.ycor() - goal.ycor()) < 20:
        level += 1
        if level > len(backdrops):
            pen.clear()
            wn.bgcolor("black")
            pen.color("white")
            pen.write("🎉 You Win! 🎉", align="center", font=("Arial", 28, "bold"))
            break
        load_level(level)
        time.sleep(0.5)
