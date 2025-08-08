import turtle

# --- Setup screen ---
screen = turtle.Screen()
screen.title("Maze Escape Game")
screen.bgcolor("black")
screen.setup(width=600, height=600)

# --- Create player ---
player = turtle.Turtle()
player.shape("turtle")
player.color("green")
player.penup()
player.speed(0)  # Instant movement

# --- Create goal ---
goal = turtle.Turtle()
goal.shape("circle")
goal.color("gold")
goal.penup()
goal.goto(250, 250)

# --- Wall data ---
walls = [
    (-300, 200, 600, 20),  # top wall
    (-300, -200, 600, 20),  # bottom wall
    (-300, -200, 20, 420),  # left wall
    (280, -200, 20, 420),   # right wall
    (-100, 100, 200, 20),   # middle wall
    (0, -100, 20, 200),     # vertical wall
]

# --- Create walls ---
wall_list = []

for x, y, width, height in walls:
    wall = turtle.Turtle()
    wall.hideturtle()
    wall.shape("square")
    wall.color("white")
    wall.shapesize(stretch_wid=height/20, stretch_len=width/20)
    wall.penup()
    wall.goto(x + width / 2, y + height / 2)
    wall.showturtle()
    wall_list.append(wall)

# --- Movement / Glide ---
MOVE_DISTANCE = 20

def can_move(new_x, new_y):
    # Check collision with walls
    for wall in wall_list:
        if wall.distance(new_x, new_y) < 25:
            return False
    return True

def move(dx, dy):
    new_x = player.xcor() + dx
    new_y = player.ycor() + dy
    if can_move(new_x, new_y):
        player.setheading(player.towards(new_x, new_y))
        player.goto(new_x, new_y)

def move_up():
    move(0, MOVE_DISTANCE)

def move_down():
    move(0, -MOVE_DISTANCE)

def move_left():
    move(-MOVE_DISTANCE, 0)

def move_right():
    move(MOVE_DISTANCE, 0)

# --- Key bindings ---
screen.listen()
screen.onkeypress(move_up, "Up")
screen.onkeypress(move_down, "Down")
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")

# --- Win check ---
def check_win():
    if player.distance(goal) < 20:
        goal.color("lime")
        player.hideturtle()
        goal.write("You Escaped!", align="center", font=("Arial", 18, "bold"))
    else:
        screen.ontimer(check_win, 100)

check_win()

# --- Keep window open ---
turtle.done()
