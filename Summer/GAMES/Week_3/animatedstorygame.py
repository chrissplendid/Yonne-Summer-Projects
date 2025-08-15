import turtle
import time

# --- Screen setup ---
wn = turtle.Screen()
wn.title("🐉 Animated Story Game")
wn.bgcolor("lightblue")
wn.setup(width=800, height=600)

# --- Hero setup ---
hero = turtle.Turtle()
hero.shape("square")  # starting costume (built-in)
hero.color("blue")
hero.penup()
hero.goto(-350, -100)

# --- Dragon setup ---
dragon = turtle.Turtle()
dragon.shape("circle")  # built-in
dragon.color("green")
dragon.penup()
dragon.hideturtle()  # will appear later
dragon.goto(200, -100)

# --- Narrator pen ---
narrator = turtle.Turtle()
narrator.hideturtle()
narrator.penup()
narrator.goto(0, 250)

def say(text):
    """Display narration text at the top."""
    narrator.clear()
    narrator.write(text, align="center", font=("Arial", 18, "bold"))

# --- Scene 1: Hero walks in ---
say("Our hero begins his journey...")
for _ in range(35):
    hero.forward(10)
    time.sleep(0.05)  # walking animation timing

# --- Scene 2: Dragon appears ---
say("A wild dragon appears!")
dragon.showturtle()
time.sleep(2)

# --- Scene 3: Hero changes costume to battle mode ---
say("The hero prepares for battle!")
hero.shape("triangle")  # built-in battle mode costume
time.sleep(2)

# --- Scene 4: Dragon flees ---
say("The dragon runs away!")
for _ in range(25):
    dragon.forward(15)
    time.sleep(0.05)
dragon.hideturtle()

# --- Scene 5: Victory ---
say("🏆 Victory! The hero saved the day!")
time.sleep(3)

wn.bye()  # Close window after story ends
