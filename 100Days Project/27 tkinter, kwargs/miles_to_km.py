from tkinter import *


def converter(a):
    a *= 1.609
    return round(a)


def button_clicked():
    new_text = converter(float(user_input.get()))
    label_ans.config(text=new_text)


ans = 0
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

user_input = Entry(width=10)
user_input.grid(column=1, row=0)

label_1 = Label(text="Miles")
label_1.grid(column=2, row=0)
label_1.config(padx=10, pady=3)

label_2 = Label(text="is equal to")
label_2.grid(column=0, row=1)

label_ans = Label(text=f"{ans}")
label_ans.grid(column=1, row=1)

label_4 = Label(text="Km")
label_4.grid(column=2, row=1)

button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)


window.mainloop()
