from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzer")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        right_image = PhotoImage(file="./images/true.png")
        wrong_image = PhotoImage(file="./images/false.png")

        self.canvas = Canvas(width=300, heigh=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some Question Text",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.right_button = Button(image=right_image, highlightthickness=0, command=self.true_pressed)
        self.right_button.grid(column=0, row=2)

        self.wrong_button = Button(image=wrong_image, highlightthickness=0, command=self.false_pressed)
        self.wrong_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.right_button.config(state="active")
            self.wrong_button.config(state="active")
        else:
            self.canvas.itemconfig(self.question_text, text=f"You've reached the end of the quiz. Your score is {self.quiz.score}/10")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.right_button.config(state="disabled")
        self.wrong_button.config(state="disabled")
        self.window.after(1000, self.get_next_question)
