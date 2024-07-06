import tkinter as tk
from tkinter import simpledialog, messagebox
import random

class GuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Guess the Number")
        upperbound=random.randint(50,500)
        self.number_to_guess = random.randint(1, upperbound)
        self.attempts = 0
        
        self.label_instruction = tk.Label(root, text="The number generated is between 1 and "+str(upperbound))
        self.label_instruction.pack(pady=20)
        
        self.button_start = tk.Button(root, text="Start ", command=self.start)
        self.button_start.pack(pady=20)
        
        self.button_exit = tk.Button(root, text="Exit", command=root.quit)
        self.button_exit.pack(pady=20)

    def start(self):
        while True:
            guess = simpledialog.askstring("Input", "Enter your number:")
            
            if guess is None:  
                break
            
            try:
                guess = int(guess)
                self.attempts += 1
                if guess < self.number_to_guess:
                    messagebox.showinfo("Result", "Too low! Try again.")
                elif guess > self.number_to_guess:
                    messagebox.showinfo("Result", "Too high! Try again.")
                else:
                    messagebox.showinfo("Result", f"Correct|! You've guessed the number {self.number_to_guess} correctly in  {self.attempts} attempts !!")
                    break
            except ValueError:
                messagebox.showerror("Invalid input", "Please enter a valid number.")

if __name__ == "__main__":
    root = tk.Tk()
    game = GuessingGame(root)
    root.mainloop()
