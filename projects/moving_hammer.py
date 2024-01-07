# Snake Game
import turtle # Built in module in Python3 which can be used to develop 2d Game
import random
import time

# Set up the screen
screen = turtle.Screen()
screen.title('Snake Game')
screen.bgcolor('black')
screen.setup(width=600, height=600)

# Set up the snake
snake = turtle.Turtle()
snake.shape('square')
snake.color('white')
snake.penup()
snake.speed(0)

# Set up the food
food = turtle.Turtle()
food.shape('circle')
food.color('blue')
food.penup()
food.speed(0)

# Set snake and food position
snake.goto(0, 0)
food.goto(random.randint(-290, 290), random.randint(-290, 290))

# Snake functions to move forward, backward, up and down
def move_up():
    snake.setheading(90)

def move_down():
    snake.setheading(-90)

def move_left():
    snake.setheading(180)

def move_right():
    snake.setheading(0)


# Movement functions to keys

screen.listen()
screen.onkey(move_up, 'Up')
screen.onkey(move_down, 'Down')
screen.onkey(move_left, 'Left')
screen.onkey(move_right, 'Right')


# Run the Game
# Conditions - to check if snake touches the screen boundary
# Print message "Game Over"

while True:
    # Move the snake
    snake.forward(10)
    time.sleep(0.1)
    # Snake and food collision
    if snake.distance(food) < 20:
        food.goto(random.randint(-290, 290), random.randint(-290, 290))

    # Snake and boundary collision
    if snake.xcor() > 290 or snake.xcor() < -290 or snake.ycor() > 290 or snake.ycor() < -290:
        break


# Message
message = turtle.Turtle()
message.color('white')
message.write('Game Over', align='center', font=('Arial', 24, 'normal'))

# Hide the snake and food
snake.hideturtle()
food.hideturtle()

# Kee the screen open till the user close
turtle.mainloop()





















