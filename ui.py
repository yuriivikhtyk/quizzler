from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"


class UI:
    def __init__(self, quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.main_canvas = Canvas(width=300, height=250, bg="white")
        self.question = self.main_canvas.create_text(150, 125, width=280, text="Question", fill="black", font=("Arial", 20, "italic"))
        self.main_canvas.grid(column=1,row=2, columnspan=2, pady=50)


        right_img = PhotoImage(file="images/true.png")
        wrong_img = PhotoImage(file="images/false.png")
        self.true_button = Button(image=right_img, highlightthickness=0, command=self.true)
        self.false_button = Button(image=wrong_img, highlightthickness=0, command=self.false)
        self.true_button.grid(column=1, row=3)
        self.false_button.grid(column=2, row=3)


        self.score_label = Label(text=f"Score: {self.quiz.score}", fg="white", background=THEME_COLOR)
        self.score_label.grid(column=2, row=1)
        

        self.get_next_question()
        
        self.window.mainloop()
    
    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.main_canvas.config(bg="white")
            q_text = self.quiz.next_question()
            self.main_canvas.itemconfig(self.question, text=q_text)
        else:
            self.main_canvas.itemconfig(self.question, text=f"You have finished quiz, your result is {self.quiz.score} out of 10.")
            self.false_button.config(state="disabled")
            self.true_button.config(state="disabled")

    def true(self):
        is_right = self.quiz.check_answer('True')
        self.feedback(is_right)

    def false(self):
        is_right = self.quiz.check_answer('False')
        self.feedback(is_right)

    def feedback(self, result):
        self.score_label.config(text=f"Score: {self.quiz.score}")
        if result == "correct":
            print("feedback - correct")
            self.main_canvas.config(bg="green")
            self.window.after(1000, self.get_next_question)
        else:
            print("feedback - wrong")
            self.main_canvas.config(bg="red")
            self.window.after(1000, self.get_next_question)
