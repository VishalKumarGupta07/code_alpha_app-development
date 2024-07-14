import tkinter as tk
from tkinter import messagebox
import random

class FlashcardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Flashcard Quiz App")
        self.flashcards = {}

        self.question_label = tk.Label(root, text="", wraplength=400)
        self.question_label.pack()

        self.answer_entry = tk.Entry(root, width=50)
        self.answer_entry.pack()

        self.check_button = tk.Button(root, text="Check", command=self.check_answer)
        self.check_button.pack()

        self.add_button = tk.Button(root, text="Add Flashcard", command=self.add_flashcard)
        self.add_button.pack()

        self.score_label = tk.Label(root, text="Score: 0/0")
        self.score_label.pack()

        self.score = 0
        self.total_questions = 0

        self.get_random_question()

    def add_flashcard(self):
        add_window = tk.Toplevel(self.root)
        add_window.title("Add Flashcard")

        question_label = tk.Label(add_window, text="Question:")
        question_label.pack()
        question_entry = tk.Entry(add_window, width=50)
        question_entry.pack()

        answer_label = tk.Label(add_window, text="Answer:")
        answer_label.pack()
        answer_entry = tk.Entry(add_window, width=50)
        answer_entry.pack()

        def save_flashcard():
            question = question_entry.get()
            answer = answer_entry.get()
            if question and answer:
                self.flashcards[question] = answer
                add_window.destroy()
            else:
                messagebox.showerror("Error", "Please fill in both question and answer")

        save_button = tk.Button(add_window, text="Save", command=save_flashcard)
        save_button.pack()

    def get_random_question(self):
        if self.flashcards:
            question = random.choice(list(self.flashcards.keys()))
            self.question_label.config(text=question)
            self.answer_entry.delete(0, tk.END)
        else:
            self.question_label.config(text="No flashcards added yet!")

    def check_answer(self):
        answer = self.answer_entry.get()
        question = self.question_label.cget("text")
        if question in self.flashcards:
            if answer.lower() == self.flashcards[question].lower():
                self.score += 1
                messagebox.showinfo("Correct!", "Your answer is correct!")
            else:
                messagebox.showinfo("Incorrect", f"Sorry, the correct answer is {self.flashcards[question]}")
            self.total_questions += 1
            self.score_label.config(text=f"Score: {self.score}/{self.total_questions}")
            self.get_random_question()
        else:
            messagebox.showerror("Error", "No question to check!")

root = tk.Tk()
app = FlashcardApp(root)
root.mainloop()