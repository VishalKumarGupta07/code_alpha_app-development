import tkinter as tk
import random
import webbrowser

class QuoteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Quote Generator")
        self.root.geometry("400x200")

        self.quotes = [
            "The only way to do great work is to love what you do. - Steve Jobs",
            "Believe you can and you're halfway there. - Theodore Roosevelt",
            "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
            "The harder I work, the luckier I get. - Gary Player",
            "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
            "The way to get started is to quit talking and begin doing. - Walt Disney",
            "If life were predictable it would cease to be life, and be without flavor. - Eleanor Roosevelt",
            "Life is what happens when you're busy making other plans. - John Lennon",
            "Spread love everywhere you go. Let no one ever come to you without leaving happier. - Mother Teresa",
            "When you reach the end of your rope, tie a knot and hang on. - Franklin D. Roosevelt",
        ]

        self.quote_label = tk.Label(root, text="", wraplength=400)
        self.quote_label.pack()

        self.new_quote_button = tk.Button(root, text="New Quote", command=self.get_new_quote)
        self.new_quote_button.pack()

        self.share_button = tk.Button(root, text="Share", command=self.share_quote)
        self.share_button.pack()

        self.get_new_quote()

    def get_new_quote(self):
        quote = random.choice(self.quotes)
        self.quote_label.config(text=quote)

    def share_quote(self):
        quote = self.quote_label.cget("text")
        url = f"https://twitter.com/intent/tweet?text={quote}"
        webbrowser.open(url)

root = tk.Tk()
app = QuoteApp(root)
root.mainloop()