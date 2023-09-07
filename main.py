import time
from snake import Snake
from turtle import Screen
from food import Food
from score import Score

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("The Legendary Snake")
screen.tracer(0)


game_is_on = True
snake = Snake()
food = Food()
score = Score()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.general_move()

    if snake.segments[0].distance(food) < 15:
        food.refresh()
        score.increase()
        new_cor = (snake.segments[-1].xcor(),snake.segments[-1].ycor())
        snake.new_segment(new_cor)


    if snake.segments[0].xcor() > 295 or snake.segments[0].xcor() < -295 or snake.segments[0].ycor() < -295 or snake.segments[0].ycor() > 295:
        game_is_on = False
        score.clear()
        score.write(f"You have lost, your final score is {score.number}", move=False, align="center", font=("Arial", 18, "normal"))


    for seg in snake.segments:
        if seg == snake.segments[0]:
            pass
        elif snake.segments[0].distance(seg) < 10:
            game_is_on = False
            score.clear()
            score.write(f"You have lost, your final score is {score.number}", move=False, align="center", font=("Arial", 18, "normal"))


screen.exitonclick()