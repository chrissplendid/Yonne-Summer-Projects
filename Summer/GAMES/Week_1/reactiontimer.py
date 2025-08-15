import turtle
import random
import time

# --- Setup screen ---
screen = turtle.Screen()
screen.title("Reaction Timer Game")
screen.bgcolor("black")

# --- Create turtle sprite ---
reactor = turtle.Turtle()
reactor.shape("circle")
reactor.color("red")
reactor.penup()
reactor.goto(0, 0)
reactor.shapesize(5)

# --- Timer display turtle ---
timer_writer = turtle.Turtle()
timer_writer.hideturtle()
timer_writer.penup()
timer_writer.color("white")
timer_writer.goto(0, 150)

# --- Variables ---
game_started = False
start_time = 0

# --- Function: show message ---
def show_message(msg):
    timer_writer.clear()
    timer_writer.write(msg, align="center", font=("Arial", 24, "bold"))

# --- Function: start the game ---
def start_game():
    global game_started, start_time

    show_message("Wait for GREEN...")
    reactor.color("red")

    # Wait random time before reacting
    delay = random.randint(2, 5)
    screen.ontimer(trigger_reaction, delay * 1000)

# --- Broadcast: Show green and start timer ---
def trigger_reaction():
    global game_started, start_time
    reactor.color("green")
    start_time = time.time()
    game_started = True
    show_message("CLICK NOW!")

# --- Event: when clicked ---
def handle_click(x, y):
    global game_started

    if reactor.color()[0] == "green" and game_started:
        reaction_time = time.time() - start_time
        show_message(f"Reaction Time: {round(reaction_time, 3)}s")
        reactor.color("blue")
        game_started = False
    elif reactor.color()[0] == "red":
        show_message("Too Early! Wait for GREEN.")
        reactor.color("gray")
        game_started = False
    else:
        show_message("Game Over")

    # Restart after 3 seconds
    screen.ontimer(start_game, 3000)

# --- Bind click event ---
reactor.onclick(handle_click)

# --- Start game ---
start_game()

# --- Mainloop ---
turtle.done()
