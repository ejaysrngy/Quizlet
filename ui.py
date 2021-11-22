THEME_COLOR = "#375362"

from tkinter import *
from quiz_brain import QuizBrain

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.content = Canvas(self.window,
                        height=300,
                        width=250,
                        highlightthickness=0,
                        bg="#537d93"
                            )
        self.button_div = Canvas(self.window,
                                 height=100,
                                 width= 250,
                                 highlightthickness=0,
                                 bg="#375362")
        self.window.title("Quizzes")
        self.window.configure(background="#375362")

        self.window.geometry("350x500")

        self.true_png = PhotoImage(file="./images/true.png")
        self.false_png = PhotoImage(file="./images/false.png")

        self.question_text = self.content.create_text(
                            125, 150,
                            width=200,
                            text="",
                            font=("Montserrat, 18")
                                )

        self.content.place(relx=0.5, rely=0.4, anchor="center")
        self.button_div.place(relx=0.5, rely=0.815, anchor="center")

        self.button_true = Button(self.button_div,
                                      text='',
                                      image=self.true_png,
                                      highlightthickness=0,
                                      bd=0,
                                      command=self.press_true
                                  )
        self.button_true.place(relx=0.8, rely=0.5, anchor="center")
        self.button_false = Button(self.button_div,
                                  text='',
                                  image=self.false_png,
                                  highlightthickness=0,
                                  bd=0,
                                  command=self.press_false
                                  )
        self.button_false.place(relx=0.2, rely=0.5, anchor="center")
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.content.config(bg="#537d93")
        q_text = self.quiz.next_question()
        self.content.itemconfig(self.question_text,
                                text=q_text)

    def press_true(self):
        self.give_feedback(self.quiz.check_answer("true"))

    def press_false(self):
        self.give_feedback(self.quiz.check_answer("false"))
        self.content.config(bg="red")

    def give_feedback(self, answer):
        if answer:
            self.content.config(bg="green")
        else:
            self.content.config(bg="red")
        self.window.after(1000, self.get_next_question)