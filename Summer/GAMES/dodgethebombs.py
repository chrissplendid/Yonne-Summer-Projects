import turtle
import random
import time

# --- Screen setup ---
wn = turtle.Screen()
wn.title("💣 Dodge the Bombs")
wn.bgcolor("skyblue")
wn.setup(width=800, height=700)
wn.tracer(0)

# --- Player setup ---
player = turtle.Turtle()
player.shape("triangle")
player.color("blue")
player.penup()
player.goto(0, -250)

# --- Bomb setup ---
bombs = []
for _ in range(5):  # number of bombs
    bomb = turtle.Turtle()
    bomb.shape("circle")
    bomb.color("red")
    bomb.penup()
    bomb.goto(random.randint(-380, 380), random.randint(100, 300))
    bomb.speed = random.randint(1, 1)  # falling speed
    bombs.append(bomb)

# --- Score ---
score = 0
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.goto(0, 260)
pen.color("black")
pen.write(f"Score: {score}", align="center", font=("Arial", 17, "bold"))

# --- Movement ---
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

wn.listen()
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")

# --- Collision check ---
def is_collision(t1, t2):
    return t1.distance(t2) < 20  # if touching radius

# --- Main game loop ---
game_over = False
start_time = time.time()

while not game_over:
    wn.update()

    for bomb in bombs:
        # Move the bomb down
        bomb.sety(bomb.ycor() - bomb.speed)

        # Reset bomb if it goes off-screen
        if bomb.ycor() < -300:
            bomb.goto(random.randint(-380, 380), random.randint(250, 300))
            score += 1
            pen.clear()
            pen.write(f"Score: {score}", align="center", font=("Arial", 18, "bold"))

        # Check collision
        if is_collision(player, bomb):
            player.color("red")
            pen.clear()
            pen.write("💥 Game Over! 💥", align="center", font=("Arial", 24, "bold"))
            game_over = True
            break

    # Speed up bombs over time
    if time.time() - start_time > 10:
        for bomb in bombs:
            bomb.speed += 1
        start_time = time.time()

wn.mainloop()
