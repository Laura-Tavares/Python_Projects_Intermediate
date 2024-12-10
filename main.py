import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "./blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

import pandas
data = pandas.read_csv("./50_states.csv")
correct_states = data["state"].tolist()
guessed_states = []

number_correct_states = 0
# while number_correct_states != 50:
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{number_correct_states}/50 States",
                                prompt="What´s another state´s name?").title()

    if answer_state == "Exit":
        missing_states = []
        for state in correct_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in correct_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()

        state_data = data[data.state == answer_state]
        t.goto(float(state_data.x.item()), float(state_data.y.item()))
        t.write(f"{answer_state}")

        guessed_states.append(answer_state)
        number_correct_states += 1

# screen.exitonclick()

# with open("states_track.txt") as f:
    # f.write(f"{guessed_states}")