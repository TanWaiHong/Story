import pandas
from tkinter import *
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/raw_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="English", fill="black")
    canvas.itemconfig(card_word, text=current_card["English"], fill="black")
    canvas.itemconfig(card_background, image=CARD_FRONT)
    window.after(3000, func=flip_card)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="Chinese", fill="white")
    canvas.itemconfig(card_word, text=current_card["Chinese"], fill="white")
    canvas.itemconfig(card_background, image=CARD_BACK)


def is_known():
    to_learn.remove(current_card)
    new_data = pandas.DataFrame(to_learn)
    new_data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# ---------------------------------- UI setup ---------------------------------#

# Window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# Image
RIGHT_IMAGE = PhotoImage(file="./images/right.png")
WRONG_IMAGE = PhotoImage(file="./images/wrong.png")
CARD_FRONT = PhotoImage(file="./images/card_front.png")
CARD_BACK = PhotoImage(file="./images/card_back.png")

# Canvas
canvas = Canvas(width=800, heigh=526)
card_background = canvas.create_image(400, 263, image=CARD_FRONT)
card_title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# Button
unknown_button = Button(image=WRONG_IMAGE, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

known_button = Button(image=RIGHT_IMAGE, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()
