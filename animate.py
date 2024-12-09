# Import pgzrun to run the Pygame Zero framework
import pgzrun

# Set up the screen dimensions
WIDTH = 500
HEIGHT = 300

# Define the ball Actor
ball = Actor('apple')  # Assumes you have an image named 'ball.png' in the same directory
ball.pos = 50, HEIGHT // 2  # Start position of the ball

# Function to animate the ball moving to the right side of the screen
def start_animation():
    # Move the ball to the right edge over 3 seconds
    animate(ball, pos=(WIDTH - 50, HEIGHT // 2), duration=3)

# Called automatically by Pygame Zero to draw the frame
def draw():
    screen.clear()
    ball.draw()

# Called once when the game starts
def on_key_down():
    start_animation()

# Run the pgzero engine
pgzrun.go()
