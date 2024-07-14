import tkinter as tk
from tkinter import messagebox
import random

class LanguageLearningApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Language Learning App")
        self.root.geometry("800x600")

        self.language = "Spanish"
        self.lessons = {
            "Lesson 1": ["Hello?", " how are u?", "hmm.."],
            "Lesson 2": ["its done the second lesson...?", "ohk..."],
            "Lesson 3": ["add your own lessons ", "ohk ", "¿done?"],
        }
        self.quizzes = {
            "Quiz 1": [[" ", "Hello, how are you?"], [" ", "Where is...?"], [" ", "My name is..."]],
            "Quiz 2": [[" ?", "How much does it cost?"], ["¿ ?", "Where can I find...?"], [" ", "I would like..."]],
            "Quiz 3": [["¿ ?", "What time is it?"], ["¿ ?", "What is your phone number?"], ["¿ ?", "Where do you live?"]],
        }
        self.progress = {"Lesson 1": False, "Lesson 2": False, "Lesson 3": False}
        self.achievements = []

        self.lesson_frame = tk.Frame(root)
        self.lesson_frame.pack()

        self.lesson_label = tk.Label(self.lesson_frame, text="Lessons", font=("Arial", 24))
        self.lesson_label.pack()

        self.lesson_listbox = tk.Listbox(self.lesson_frame, width=40)
        self.lesson_listbox.pack()
        for lesson in self.lessons.keys():
            self.lesson_listbox.insert(tk.END, lesson)

        self.start_button = tk.Button(self.lesson_frame, text="Start Lesson", command=self.start_lesson)
        self.start_button.pack()

        self.quiz_frame = tk.Frame(root)
        self.quiz_frame.pack()

        self.quiz_label = tk.Label(self.quiz_frame, text="Quizzes", font=("Arial", 24))
        self.quiz_label.pack()

        self.quiz_listbox = tk.Listbox(self.quiz_frame, width=40)
        self.quiz_listbox.pack()
        for quiz in self.quizzes.keys():
            self.quiz_listbox.insert(tk.END, quiz)

        self.take_quiz_button = tk.Button(self.quiz_frame, text="Take Quiz", command=self.take_quiz)
        self.take_quiz_button.pack()

        self.progress_frame = tk.Frame(root)
        self.progress_frame.pack()

        self.progress_label = tk.Label(self.progress_frame, text="Progress", font=("Arial", 24))
        self.progress_label.pack()

        self.progress_listbox = tk.Listbox(self.progress_frame, width=40)
        self.progress_listbox.pack()
        for lesson, completed in self.progress.items():
            self.progress_listbox.insert(tk.END, f"{lesson}: {completed}")

        self.achievements_frame = tk.Frame(root)
        self.achievements_frame.pack()

        self.achievements_label = tk.Label(self.achievements_frame, text="Achievements", font=("Arial", 24))
        self.achievements_label.pack()

        self.achievements_listbox = tk.Listbox(self.achievements_frame, width=40)
        self.achievements_listbox.pack()
        for achievement in self.achievements:
            self.achievements_listbox.insert(tk.END, achievement)

        self.forum_button = tk.Button(root, text="Community Forum", command=self.open_forum)
        self.forum_button.pack()

    def start_lesson(self):
        lesson = self.lesson_listbox.get(self.lesson_listbox.curselection())
        lesson_text = "\n\n".join(self.lessons[lesson])
        messagebox.showinfo("Lesson", lesson_text)

    def take_quiz(self):
        quiz = self.quiz_listbox.get(self.quiz_listbox.curselection())
        score = 0
        for question, answer in self.quizzes[quiz]:
            user_answer = input(f"{question}: ")
            if user_answer.lower() == answer.lower():
                score += 1
        messagebox.showinfo("Quiz Result", f"You scored {score}/{len(self.quizzes[quiz])} on the quiz!")

    def open_forum(self):
        messagebox.showinfo("Community Forum", "Welcome to the community forum! This is where you can discuss language learning with other users.")

root = tk.Tk()
app = LanguageLearningApp(root)
root.mainloop()