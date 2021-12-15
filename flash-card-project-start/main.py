BACKGROUND_COLOR = "#B1DDC6"
import tkinter
import pandas
import random
from os.path import exists
import requests


learn_path = exists("words_to_learn.csv")
print(learn_path)

if learn_path:
    word_data = pandas.read_csv("words_to_learn.csv")
else:
    word_data = pandas.read_csv("data/french_words.csv")

random_value = random.randint(0, len(word_data["French"]))
fr_word = word_data["French"][random_value]
index_to_remove = []
print(word_data["English"][random_value] + "|" + word_data["French"][random_value])

# -------------------------DATA------------------------------

def random_fr_word():
    global random_value, flip_timer, fr_word
    window.after_cancel(flip_timer)
    random_value = random.randint(0, len(word_data["French"]))
    fr_word = word_data["French"][random_value]
    canvas.itemconfig(word, fill="black", text=fr_word)
    canvas.itemconfig(language, fill="black", text="French")
    canvas.itemconfig(canvas_image, image=french_img)
    print(word_data["English"][random_value] + "|" + word_data["French"][random_value])
    flip_timer = window.after(3000, english_card)
    return fr_word

def english_card():
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(canvas_image, image=english_img)
    eng_word = word_data["English"][random_value]
    canvas.itemconfig(word, fill="white", text=eng_word)

def remove_card():
    global word_data
    index_to_remove.append(random_value)
    print(f"CARD TO REMOVE: {word_data['French'][random_value]}")
    print(index_to_remove)
    words_to_learn = word_data.drop(word_data.index[index_to_remove])
    words_to_learn.to_csv("words_to_learn.csv")
    random_fr_word()

# -------------------------UI------------------------------

window = tkinter.Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, english_card)

canvas = tkinter.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
french_img = tkinter.PhotoImage(file="images/card_front.png")
english_img = tkinter.PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=french_img)
language = canvas.create_text(400, 150, text="French", fill="black", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text=fr_word, fill="black", font=("Ariel", 40, "bold"))
canvas.grid(column=0, row=0, columnspan=2, rowspan=2)

wrong_img = tkinter.PhotoImage(file="images/wrong.png")
wrong_button = tkinter.Button(image=wrong_img, bg=BACKGROUND_COLOR, highlightthickness=0, command=random_fr_word)
wrong_button.grid(column=0, row=2)

right_img = tkinter.PhotoImage(file="images/right.png")
right_button = tkinter.Button(image=right_img, bg=BACKGROUND_COLOR, highlightthickness=0, command=remove_card)
right_button.grid(column=1, row=2)


window.mainloop()
