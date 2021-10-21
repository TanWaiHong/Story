import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = list()

the_turtle = turtle.Turtle()
the_turtle.penup()
the_turtle.hideturtle()

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 State Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    else:
        current_answer_state = data[data.state == f"{answer_state}"]

        if current_answer_state.empty:
            print("no")
        else:
            if answer_state not in guessed_states:
                guessed_states.append(answer_state)
                current_position = (current_answer_state.x.item(), current_answer_state.y.item())
                the_turtle.goto(current_position)
                the_turtle.write(answer_state, align="center", font=("Courier", 8, "normal"))

            else:
                print("oi")

screen.exitonclick()
