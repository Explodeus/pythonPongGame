# By @VSokha

# Initializations
import turtle

window = turtle.Screen()
window.title('Pong')
window.bgcolor('black')
window.setup(width=800, height=600)
window.tracer(0)


# Game models
## Paddle A
paddle_a = turtle.Turtle()
## Paddle B 
paddle_b = turtle.Turtle()
## Ball
ball = turtle.Turtle()

# Main loop
while True:
    window.update()