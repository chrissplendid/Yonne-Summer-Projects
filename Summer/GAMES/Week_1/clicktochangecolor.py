import turtle
import random
import time

# Set up the screen
screen = turtle.Screen()
screen.title("Click to Change Color Game")
screen.bgcolor("white")
screen.setup(width=600, height=600)

# Create the main character (sprite)
player = turtle.Turtle()
player.shape("turtle")
player.color("blue")
player.penup()
player.shapesize(3)

# Create a turtle to display score
score_writer = turtle.Turtle()
score_writer.hideturtle()
score_writer.penup()
score_writer.goto(0, 260)
score_writer.write("Score: 0", align="center", font=("Arial", 20, "bold"))

# Variables
score = 0
colors = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "cyan"]

# Function to update score on screen
def update_score():
    score_writer.clear()
    score_writer.write(f"Score: {score}", align="center", font=("Arial", 20, "bold"))

# Function to handle click
def on_click(x, y):
    global score
    # Change turtle color
    new_color = random.choice(colors)
    player.color(new_color)
    
    # Move to random position
    new_x = random.randint(-250, 250)
    new_y = random.randint(-250, 250)
    player.goto(new_x, new_y)

    # Increase score
    score += 1
    update_score()
    print(f"Turtle clicked! New color: {new_color}, Score: {score}")

# Bind click event
player.onclick(on_click)

# OPTIONAL: Timer (uncomment to use)
# def end_game():
#     player.hideturtle()
#     screen.bye()
#     print("Time's up! Final Score:", score)

# screen.ontimer(end_game, 20000)  # Ends game after 20 seconds

# Keep the game running
turtle.done()
