import tkinter as tk
from tkinter import messagebox
import random

# Questions and Answers
questions = [
    {
        "question": "What is the default package manager for Debian?",
        "options": ["Flatpaks", "APT", "ATP", "Pac-Man"],
        "answer": "APT",
    },
      {
        "question": "Which command lists files and folders/directories",
        "options": ["Direc", "list", "ls", "dir"],
        "answer": "ls",
    },
          {
        "question": "What does 'cd' do",
        "options": ["Open the CD-ROM drive", "Change the directory", "Create a directory", "Change the disks partition table"],
        "answer": "Change the directory",
    },
          {
        "question": "which command displays what is in a file",
        "options": ["cat", "dog", "follow", "view"],
        "answer": "cat",
    },   
          {
        "question": "How do you make a directory",
        "options": ["nwdir", "mvdir", "mkidfk", "mkdir"],
        "answer": "mkdir",
    },  
  


]

# Randomize the question order
random.shuffle(questions)

# Initialize Variables
current_question_index = 0
score = 0

# Functions
def load_question():
    """Load the current question and options."""
    question_label.config(text=questions[current_question_index]["question"])
    options = questions[current_question_index]["options"]
    for i, option in enumerate(options):
        radio_buttons[i].config(text=option, value=option)
    answer_var.set("")  # Reset selection

def next_question():
    """Handle the Next button click."""
    global current_question_index, score

    # Check the answer
    selected_answer = answer_var.get()
    if selected_answer == questions[current_question_index]["answer"]:
        score += 1

    # Move to the next question or end the quiz
    current_question_index += 1
    if current_question_index < len(questions):
        load_question()
    else:
        # End of quiz
        messagebox.showinfo("Quiz Completed", f"You scored {score}/{len(questions)}")
        root.quit()

def quit_quiz():
    """Quit the quiz with confirmation."""
    if messagebox.askyesno("Quit Quiz", "Are you sure you want to quit?"):
        root.quit()

# Create the main application window
root = tk.Tk()
root.title("Quiz App")
root.geometry("400x300")

# Question Label
question_label = tk.Label(root, text="", wraplength=350, font=("Arial", 12), justify="center")
question_label.pack(pady=20)

# Answer Buttons
answer_var = tk.StringVar(value="")
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

radio_buttons = []
for i in range(4):
    rb = tk.Radiobutton(
        button_frame,
        text="",
        variable=answer_var,
        value="",
        font=("Arial", 10),
        wraplength=350,
        justify="left",
    )
    rb.pack(anchor="w")
    radio_buttons.append(rb)

# Navigation Buttons
nav_frame = tk.Frame(root)
nav_frame.pack(pady=20)

next_button = tk.Button(nav_frame, text="Next", command=next_question)
next_button.pack(side="left", padx=10)

quit_button = tk.Button(nav_frame, text="Quit", command=quit_quiz)
quit_button.pack(side="right", padx=10)

# Load the first question
load_question()

# Run the main loop
root.mainloop()
