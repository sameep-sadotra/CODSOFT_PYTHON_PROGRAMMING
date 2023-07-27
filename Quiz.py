import tkinter as tk
from tkinter import messagebox
import random

# Quiz Questions and Answers
questions = {
    "math": [
        {
            "question": "What is 2 + 2?",
            "options": ["3", "4", "5"],
            "correct_answer": "4"
        },
        {
            "question": "What is the square root of 25?",
            "options": ["5", "6", "7"],
            "correct_answer": "5"
        },
        {
            "question": "Simplify: 2 * (3 + 5) - 4",
            "options": ["12", "14", "16"],
            "correct_answer": "12"
        },
        {
            "question": "What is 7 * 8?",
            "options": ["54", "56", "58"],
            "correct_answer": "56"
        },
        {
            "question": "Solve for x: 3x + 10 = 25",
            "options": ["5", "6", "7"],
            "correct_answer": "5"
        },
    ],
    "current_affairs": [
        {
            "question": "Which country hosted the 2022 FIFA World Cup?",
            "options": ["France", "Qatar", "Brazil"],
            "correct_answer": "Qatar"
        },
        {
            "question": "Who is the current President of the United States?",
            "options": ["Joe Biden", "Donald Trump", "Barack Obama"],
            "correct_answer": "Joe Biden"
        },
        {
            "question": "What is the capital of Japan?",
            "options": ["Tokyo", "Beijing", "Seoul"],
            "correct_answer": "Tokyo"
        },
        {
            "question": "When did the COVID-19 pandemic start?",
            "options": ["2019", "2020", "2021"],
            "correct_answer": "2019"
        },
        {
            "question": "Which planet is known as the 'Red Planet'?",
            "options": ["Mars", "Venus", "Jupiter"],
            "correct_answer": "Mars"
        },
    ],
    "science": [
        {
            "question": "What is the chemical symbol for water?",
            "options": ["H2O", "CO2", "O2"],
            "correct_answer": "H2O"
        },
        {
            "question": "What is the largest organ in the human body?",
            "options": ["Heart", "Skin", "Liver"],
            "correct_answer": "Skin"
        },
        {
            "question": "What is the unit of measurement for force?",
            "options": ["Newton", "Watt", "Joule"],
            "correct_answer": "Newton"
        },
        {
            "question": "What is the process by which plants make their food?",
            "options": ["Photosynthesis", "Respiration", "Transpiration"],
            "correct_answer": "Photosynthesis"
        },
        {
            "question": "Which gas is most abundant in the Earth's atmosphere?",
            "options": ["Oxygen", "Carbon dioxide", "Nitrogen"],
            "correct_answer": "Nitrogen"
        },
    ],
    "sst": [
        {
            "question": "Who was the first President of the United States?",
            "options": ["Thomas Jefferson", "George Washington", "John Adams"],
            "correct_answer": "George Washington"
        },
        {
            "question": "What is the largest ocean on Earth?",
            "options": ["Indian Ocean", "Pacific Ocean", "Atlantic Ocean"],
            "correct_answer": "Pacific Ocean"
        },
        {
            "question": "What is the currency of Japan?",
            "options": ["Yen", "Won", "Euro"],
            "correct_answer": "Yen"
        },
        {
            "question": "Which famous scientist formulated the theory of relativity?",
            "options": ["Isaac Newton", "Albert Einstein", "Galileo Galilei"],
            "correct_answer": "Albert Einstein"
        },
        {
            "question": "Who wrote the play 'Romeo and Juliet'?",
            "options": ["William Shakespeare", "Jane Austen", "Charles Dickens"],
            "correct_answer": "William Shakespeare"
        },
    ],
    "gk": [
        {
            "question": "Which country is known as the 'Land of the Rising Sun'?",
            "options": ["China", "Japan", "India"],
            "correct_answer": "Japan"
        },
        {
            "question": "Who painted the Mona Lisa?",
            "options": ["Pablo Picasso", "Vincent van Gogh", "Leonardo da Vinci"],
            "correct_answer": "Leonardo da Vinci"
        },
        {
            "question": "What is the largest mammal in the world?",
            "options": ["Elephant", "Giraffe", "Blue Whale"],
            "correct_answer": "Blue Whale"
        },
        {
            "question": "Which planet is known as the 'Morning Star'?",
            "options": ["Venus", "Mars", "Mercury"],
            "correct_answer": "Venus"
        },
        {
            "question": "In which country is the famous Taj Mahal located?",
            "options": ["India", "Egypt", "China"],
            "correct_answer": "India"
        },
    ],
}

class QuizApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Quiz Game")
        self.geometry("400x300")
        self.configure(bg="blue")
        self.current_subject = None
        self.question_index = 0
        self.score = 0

        self.welcome_label = tk.Label(self, text="Welcome to the Quiz Game!", font=("Helvetica", 16), bg="blue")
        self.welcome_label.pack(pady=10)

        self.rules_label = tk.Label(self, text="Rules:\n1. Select the correct answer for each question.\n2. You will get immediate feedback for your answer.", font=("Helvetica", 10), bg="blue")
        self.rules_label.pack(pady=5)

        self.next_button = tk.Button(self, text="Next", fg="white", bg="green", command=self.start_quiz)
        self.next_button.pack(pady=10)

    def start_quiz(self):
        self.next_button.pack_forget()
        self.rules_label.pack_forget()

        self.subject_selection()

    def subject_selection(self):
        self.clear_screen()

        self.subject_label = tk.Label(self, text="Choose a subject:", font=("Helvetica", 12), bg="blue")
        self.subject_label.pack(pady=10)

        self.math_button = tk.Button(self, text="Math", command=lambda: self.start_subject("math"))
        self.math_button.pack(pady=5)

        self.current_affairs_button = tk.Button(self, text="Current Affairs", command=lambda: self.start_subject("current_affairs"))
        self.current_affairs_button.pack(pady=5)

        self.science_button = tk.Button(self, text="Science", command=lambda: self.start_subject("science"))
        self.science_button.pack(pady=5)

        self.sst_button = tk.Button(self, text="Social Studies", command=lambda: self.start_subject("sst"))
        self.sst_button.pack(pady=5)

        self.gk_button = tk.Button(self, text="General Knowledge", command=lambda: self.start_subject("gk"))
        self.gk_button.pack(pady=5)

        self.quit_button = tk.Button(self, text="Quit", command=self.quit)
        self.quit_button.pack(pady=10)

    def start_subject(self, subject):
        self.current_subject = subject
        random.shuffle(questions[self.current_subject])
        self.show_question()

    def show_question(self):
        if self.question_index < len(questions[self.current_subject]):
            self.clear_screen()

            question_data = questions[self.current_subject][self.question_index]
            question_text = question_data["question"]
            options = question_data["options"]

            self.question_label = tk.Label(self, text=question_text, font=("Helvetica", 12), bg="blue")
            self.question_label.pack(pady=10)

            self.answer_var = tk.StringVar()
            for i, option in enumerate(options):
                option_radio = tk.Radiobutton(self, text=option, variable=self.answer_var, value=option, bg="blue", selectcolor="green")
                option_radio.pack(anchor="w")

            self.prev_button = tk.Button(self, text="Previous", command=self.prev_question)
            self.prev_button.pack(side="left", padx=10, pady=20)

            self.next_button = tk.Button(self, text="Next", fg="white", bg="green", command=self.check_answer)
            self.next_button.pack(side="right", padx=10, pady=20)

        else:
            self.show_results()

    def prev_question(self):
        if self.question_index > 0:
            self.question_index -= 1
            self.show_question()

    def check_answer(self):
        user_answer = self.answer_var.get()
        correct_answer = questions[self.current_subject][self.question_index]["correct_answer"]

        if user_answer == correct_answer:
            self.score += 1

        self.question_index += 1
        self.show_question()

    def show_results(self):
        self.clear_screen()

        result_text = ""
        if self.score < 2:
            result_text = "Please work on it."
        elif 2 <= self.score <= 4:
            result_text = "Great job!"
        else:
            result_text = "Extraordinary! What a great mind!"

        result_label = tk.Label(self, text=f"Your Score: {self.score}\n{result_text}", font=("Helvetica", 14), bg="blue")
        result_label.pack(pady=20)

        self.play_again_button = tk.Button(self, text="Play Again", fg="white", bg="green", command=self.play_again)
        self.play_again_button.pack(pady=10)

        self.quit_button = tk.Button(self, text="Quit", fg="white", bg="red", command=self.quit)
        self.quit_button.pack(pady=10)

    def play_again(self):
        self.current_subject = None
        self.question_index = 0
        self.score = 0
        self.play_again_button.pack_forget()
        self.quit_button.pack_forget()
        self.subject_selection()

    def clear_screen(self):
        for widget in self.winfo_children():
            widget.pack_forget()

if __name__ == "__main__":
    app = QuizApp()
    app.mainloop()
