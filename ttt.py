# -------------------------------------
# Tic-Tac-Toe!
# This is a simple Tic-Tac-Toe game
# that I built while learning tkinter
# Logan Bowers
# -------------------------------------

import random
from tkinter import *
from tkinter import messagebox
global clicked
global count
clicked, count = True, 0

def end_game(): game.quit() # End the game from the options menu

# Resets and reconfigures the button grid
def reConfig():
    buttons.clear()
    global clicked
    global count
    clicked, count = True, 0
    for i in range(9):
        b = Button(game, text=" ", font=("Comfortaa", 40,),height=3, width=6, bg="SystemButtonFace", command=lambda i=i: Clicked(buttons[i], buttons))
        buttons.append(b)
        b.grid(row=i//3, column=i%3, sticky=NSEW, padx=3, pady=3)
        b.configure(bg="light gray")

# Calls helper function to check the grid and determine a winner, or no winner
def determineOutcome(b, let):
    global winner
    winner = False
    checkForWin(b, let)

# disables all buttons in the grid when outcome is determined
def disableButtons():
    for b in buttons: b.config(state=DISABLED)

# loops through list of all win conditions and checks if any of them are met
def checkForWin(b, let):
    global winner
    win_conditions = [
        [0, 1, 2],  # top row
        [3, 4, 5],  # middle row
        [6, 7, 8],  # bottom row
        [0, 3, 6],  # left column
        [1, 4, 7],  # middle column
        [2, 5, 8],  # right column
        [0, 4, 8],  # diagonal
        [2, 4, 6]   # diagonal
    ]

    for condition in win_conditions:
        if b[condition[0]]["text"] == b[condition[1]]["text"] == b[condition[2]]["text"] == let:
            for index in condition:
                b[index].config(bg="green")
            winner = True
            messagebox.showinfo("Tic-Tac-Toe:", let + " wins")
            disableButtons()
            return
    #  tie?
    if count == 9 and winner == False:
        messagebox.showinfo("Tic-Tac-Toe:", "No one wins")
        disableButtons()

# Defines what to do when a button is clicked
# Continuously checks if it can determine a winner
def Clicked(b,buttons):
    global clicked, count
    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        determineOutcome(buttons, "X")
        if count < 9 and not winner:  # AI's turn if the game is not over
            ai_move = random.choice([button for button in buttons if button["text"] == " "])
            ai_move["text"] = "O"
            clicked = True
            count += 1
            determineOutcome(buttons, "O")
    else:
        messagebox.showerror("Tic-Tac-Toe", "Box already filled\n")

game = Tk()
game.title('Tic-Tac-Toe')
game.geometry("400x400")
game.resizable(True, True)
game.configure(bg="black")

global buttons
buttons = []
reConfig()

for i in range(3):
    game.grid_rowconfigure(i, weight=1, minsize=100)
    game.grid_columnconfigure(i, weight=1, minsize=100)

menu = Menu(game)
game.config(menu=menu)

options = Menu(menu, tearoff=False)
menu.add_cascade(label="Options", menu=options)
options.add_command(label="Reset Game", command=reConfig)
options.add_command(label="Exit", command=end_game)

game.mainloop()