THEME_COLOR = "#375362"
from tkinter import *


class QuizWindow:
    def __init__(self, quiz_brain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score = Label(text="Score: 0", bg=THEME_COLOR, fg='white', font=('Arial', 12))
        self.canvas = Canvas(height=250, width=300, highlightthickness=0)
        cv_height = self.canvas.winfo_reqheight()
        cv_width = self.canvas.winfo_reqwidth()
        self.question_text = self.canvas.create_text((cv_width / 2), (cv_height / 2) - 20,
                                                     width=280,
                                                     fill=THEME_COLOR,
                                                     text='Default Text', font=('Arial', 20, 'italic'), anchor='center')

        true_image = PhotoImage(file='images/true.png')
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true)

        false_image = PhotoImage(file='images/false.png')
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false)

        self.arrange()
        self.getQuestion()
        self.window.mainloop()

    def arrange(self):
        self.score.grid(column=1, row=0, sticky='e')
        self.canvas.grid(column=0, row=1, columnspan=2, pady=30)
        self.true_button.grid(column=0, row=2)
        self.false_button.grid(column=1, row=2)

    def true(self):
        result = self.quiz.check_answer("true")
        self.user_feedback(result)

    def false(self):
        result = self.quiz.check_answer("false")
        self.user_feedback(result)


    def reset(self):
        self.canvas.config(bg='white')
        self.getQuestion()

    def user_feedback(self, result:bool):
        if result:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.score.config(text=f"Score: {self.quiz.score}")
        self.window.after(1000, self.reset)

    def getQuestion(self):
        if self.quiz.still_has_questions():
            question = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=question)
        else:
            self.gameover()

    def gameover(self):
        self.canvas.itemconfig(self.question_text,
                               text=f"You've completed the quiz!\nYour final score was: {self.quiz.score}/{self.quiz.question_number}")
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")