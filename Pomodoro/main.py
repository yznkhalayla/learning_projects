from tkinter import *
import pygame
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.01
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
pygame.mixer.init()
pygame.mixer.music.load("sonic_ring_sound_effect.mp3")


def play():
    pygame.mixer.music.play(loops=0)


def reset_timer():
    global timer
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")

    global reps
    reps = 0

    label.configure(text="Timer", fg=GREEN)
    check_marks.configure(text="")


def start_timer():
    global reps
    reps += 1

    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        label.configure(text="Break", fg=RED)
        play()
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        label.configure(text="Break", fg=PINK)
        play()
    else:
        count_down(WORK_MIN * 60)
        label.configure(text="Work", fg=GREEN)


def count_down(count):
    seconds = count % 60
    minutes = math.floor(count / 60)
    # hours = math.floor(minutes / 60)

    if seconds < 10:
        seconds = f"0{seconds}"
    if minutes < 10:
        minutes = f"0{minutes}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = ""
        sessions = math.floor(reps/2)
        for _ in range(sessions):
            marks += "✔"

        check_marks.configure(text=marks)


window = Tk()
window.title("Pomodoro")
window.configure(padx=100, pady=50, bg=YELLOW)

tomato_image = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35))
canvas.grid(row=1, column=1)

label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
label.grid(row=0, column=1)

start_button = Button(text="Start", command=start_timer, highlightthickness=0)
start_button.grid(row=2, column=0)
reset_button = Button(text="Reset", command=reset_timer, highlightthickness=0)
reset_button.grid(row=2, column=2)

check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(row=3, column=1)

window.mainloop()