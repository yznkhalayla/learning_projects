import pandas
import turtle

# def get_mouse_click_coordinates(x, y):
#     print(x, y)


screen = turtle.Screen()
screen.title("US States Game")
IMAGE = "blank_states_img.gif"
screen.addshape(IMAGE)
turtle.shape(IMAGE)

timmy = turtle.Turtle()
timmy.hideturtle()
timmy.penup()

# turtle.onscreenclick(get_mouse_click_coordinates)

data = pandas.read_csv("50_states.csv")

answer = screen.textinput(title="Guess the State", prompt="Write a State name?").title()

data_list = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:

    if answer == "Exit":
        break

    if answer in data_list:
        row = data[data["state"] == answer]
        timmy.goto(int(row["x"]), int(row["y"]))
        timmy.write(arg=row["state"].item())
        guessed_states.append(row["state"].item())

        data_list.remove(answer)

    answer = screen.textinput(title=f"{len(guessed_states)}/50", prompt="Write a State name?").title()

missed_states = pandas.DataFrame(data_list)
missed_states.to_csv("Missed States.csv")