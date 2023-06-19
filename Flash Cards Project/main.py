from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
CARD_SPEED = 1000

try:
    data = pandas.read_csv("data/to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")

    data_frame = pandas.DataFrame(data)
    data_frame.to_csv("data/to_learn.csv")
finally:
    to_learn = data.to_dict(orient="records")


try:
    data = pandas.read_csv("data/learnt.csv")
except FileNotFoundError:
    data_frame = pandas.DataFrame()
    data_frame.to_csv("data/learnt.csv")

    data = pandas.read_csv("data/learnt.csv")
finally:
    learnt = data.to_dict(orient="records")

current_card = random.choice(to_learn)


def pass_card():
    global current_card, timer
    current_card = random.choice(to_learn)

    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=front_image)
    canvas.itemconfig(card_explanation, text="")

    window.after_cancel(timer)
    timer = window.after(CARD_SPEED, func=flip_card)


def release_card():
    global current_card

    learnt.append(current_card)
    df = pandas.DataFrame(learnt)
    df.to_csv("data/learnt.csv", index=False)

    to_learn.remove(current_card)
    df = pandas.DataFrame(to_learn)
    df.to_csv("data/to_learn.csv", index=False)

    pass_card()


def flip_card():
    global current_card
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=back_image)

    canvas.itemconfig(card_explanation, text=current_card["French"])



window = Tk()
window.title("Flashy")
window.configure(padx=50, pady=50, bg=BACKGROUND_COLOR)
timer = window.after(2000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=front_image)

card_title = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text=current_card["French"], font=("Ariel", 60, "bold"))
card_explanation = canvas.create_text(400, 300, text="", font=("Ariel", 15, "italic"))

canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
no_button = Button(image=cross_image, highlightthickness=0, command=pass_card)
no_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
yes_button = Button(image=check_image, highlightthickness=0, command=release_card)
yes_button.grid(row=1, column=1)


window.mainloop()
