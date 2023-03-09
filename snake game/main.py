from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('white')
screen.title('Snake Game')

screen.tracer(0)  # blanks the graphic in the screen
snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')



game_on = True
while game_on:
    screen.update()  #shows it , we put it there cos all the segments have been
    time.sleep(0.1)  #increases the speed

    if snake.head.distance(Food) > 15:
        food.refresh()
        snake.extend()

        # detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset_snake()



        # detect colliesion with tail
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset_snake()


    snake.move_snake()






screen.exitonclick()