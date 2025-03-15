import tkinter as tk
from tkinter import messagebox

# Function to count words in the text area
def count_words():
    """Counts words in the entered text and displays the result."""
    text = text_input.get("1.0", tk.END).strip()  # Get text from the input box

    if not text:  # Check if input is empty
        messagebox.showerror("Error", "Please enter some text!")
        return

    word_count = len(text.split())  # Splitting text into words and counting them
    result_label.config(text=f"Word Count: {word_count}")  # Update the label with count

# Creating the main application window
root = tk.Tk()
root.title("Word Counter")  # Set window title
root.geometry("400x250")  # Set window size
root.resizable(False, False)  # Prevent resizing

# Heading Label
title_label = tk.Label(root, text="Simple Word Counter", font=("Arial", 14, "bold"))
title_label.pack(pady=10)

# Text input area
text_input = tk.Text(root, height=5, width=40)  # Multi-line text input
text_input.pack(pady=5)

# Button to trigger word count
count_button = tk.Button(root, text="Count Words", command=count_words, font=("Arial", 10))
count_button.pack(pady=5)

# Label to display word count result
result_label = tk.Label(root, text="Word Count: 0", font=("Arial", 12))
result_label.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
