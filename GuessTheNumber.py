# This is a simple guess the number game. 
# The computer will think of a random number from 1 to 20
# and ask the user to guess it. The user will have 6 tries
# to guess the number correctly. If the user guesses correctly
# within 6 tries, the user wins. Otherwise, the user loses.
# After guessing, the user will be notified if their number is too low or too high.
# The user will also be notified if they have won or lost.

import random as r
import tkinter as tk

# Create the window
window = tk.Tk()
window.title("Guess The Number")
window.geometry("300x100")
window.resizable(False, False)

# Create the widgets
lbl = tk.Label(window, text="Welcome, mortal! Guess a number from 1 to 20!")
lbl.pack()
entry = tk.Entry(window)
entry.pack()
btn = tk.Button(window, text="Guess!")
btn.pack()

# Create the variables
number = r.randint(1, 20)
tries = 0
win = False

# Create the functions
def guess():
    global tries
    global win
    guess = int(entry.get())
    if guess == number:
        lbl["text"] = "You guessed correctly! You win!"
        win = True
    elif guess > number:
        lbl["text"] = "Your guess is too high!"
    else:
        lbl["text"] = "Your guess is too low!"
    tries += 1
    if tries == 6 and win == False:
        lbl["text"] = "You lose! The number was " + str(number) + "!"
    entry.delete(0, "end")

# Bind the button to the function
btn["command"] = guess

# Run the window
window.mainloop()

# End of program


