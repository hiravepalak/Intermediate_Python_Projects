from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizGui:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Trivia App")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_display = Label(self.window, text="Score: 0", bg=THEME_COLOR, font=("Arial", 12, "bold"), fg="white")
        self.score_display.grid(row=0, column=1)

        self.white_box = Canvas(self.window, width=300, height=250, bg="#f0f0f0")
        self.white_box.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        self.question_text = Label(self.window, text="Some Question Text", fg=THEME_COLOR, font=("Arial", 12, "bold"),
                                   wraplength=250)
        self.question_text.grid(row=1, column=0, columnspan=2)

        self.false_photo = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.false_photo, command=self.false_clicked)
        self.false_button.grid(row=2, column=1)

        self.true_photo = PhotoImage(file="images/true.png")
        self.true_button = Button(image=self.true_photo, command=self.true_clicked)
        self.true_button.grid(row=2, column=0)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.white_box.configure(background="white")
        if self.quiz.still_has_questions():
            self.score_display.configure(text=f"Score: {self.quiz.score}")
            q_text =self.quiz.next_question()
            self.question_text.configure(text=q_text)

        else:
            self.question_text.configure(text="Finished All Questions!")
            self.true_button.configure(state=DISABLED)
            self.false_button.configure(state=DISABLED)

    def true_clicked(self):
        is_right = self.quiz.check_answer("true")
        self.give_feedback(is_right)

    def false_clicked(self):
        is_right = self.quiz.check_answer("false")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right == True:
            self.white_box.configure(background="green")
        else:
            self.white_box.configure(background="red")
        self.window.after(1000, self.get_next_question)


