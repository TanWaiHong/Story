import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle_list = list()

for turtle_index in range(6):
    turtle_list.append(Turtle(shape="turtle"))
    turtle_list[turtle_index].color(colors[turtle_index])
    turtle_list[turtle_index].penup()
    turtle_list[turtle_index].goto(x=-230, y=-100 + turtle_index * 40)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in turtle_list:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You,ve won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
                break
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
