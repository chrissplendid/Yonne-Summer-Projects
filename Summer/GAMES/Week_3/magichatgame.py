import turtle
import random

# --- Screen setup ---
wn = turtle.Screen()
wn.title("🎩 Magic Hat Game - Power-ups & Lives")
wn.bgcolor("lightblue")
wn.setup(width=800, height=600)
wn.tracer(0)  # Turn off automatic animation

# --- Variables ---
lives = 3
power_ups = 0
game_over = False

# --- Player (Magic Hat) ---
player = turtle.Turtle()
player.shape("triangle")
player.color("purple")
player.penup()
player.goto(0, -250)

# --- Create falling object template ---
object_template = turtle.Turtle()
object_template.shape("circle")
object_template.color("gold")
object_template.penup()
object_template.hideturtle()

# --- Clone falling objects ---
falling_objects = []
for _ in range(5):
    obj = object_template.clone()
    obj.goto(random.randint(-380, 380), random.randint(150, 300))
    obj.showturtle()
    falling_objects.append(obj)

# --- Status writer ---
status_writer = turtle.Turtle()
status_writer.hideturtle()
status_writer.penup()
status_writer.goto(0, 260)

def update_status():
    status_writer.clear()
    status_writer.write(
        f"Lives: {lives}   Power-ups: {power_ups}",
        align="center",
        font=("Arial", 18, "bold")
    )

update_status()

# --- Player movement ---
def move_left():
    x = player.xcor() - 30
    if x < -380: x = -380
    player.setx(x)

def move_right():
    x = player.xcor() + 30
    if x > 380: x = 380
    player.setx(x)

wn.listen()
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")

# --- Game loop ---
while not game_over:
    wn.update()

    for obj in falling_objects:
        # Move object down
        obj.sety(obj.ycor() - random.uniform(0.2, 0.3))

        # If object falls below screen, reset it to top
        if obj.ycor() < -300:
            obj.goto(random.randint(-380, 380), random.randint(200, 300))

        # Collision detection
        if player.distance(obj) < 20:
            # Random chance: power-up or lose life
            if random.random() < 0.6:  # 60% chance to gain a power-up
                power_ups += 1
            else:
                lives -= 1

            update_status()

            # Reset object to top
            obj.goto(random.randint(-380, 380), random.randint(200, 300))

    # End game condition
    if lives <= 0:
        game_over = True

# --- Game Over message ---
status_writer.goto(0, 0)
status_writer.write("GAME OVER!", align="center", font=("Arial", 28, "bold"))

wn.mainloop()
