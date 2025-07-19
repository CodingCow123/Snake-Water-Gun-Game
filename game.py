from tkinter import *
from PIL import Image, ImageTk
from random import choice
import pandas as pd

#Global variable for the player name. Initialized to nothing because we haev to declare as something. However, the value in the code will change once the user inputs their name.
playername="" 
#This code creates a window using tkinter's Tk(), sets the name of the window with .title and the size of the window in pixels with .window.
window = Tk()
window.title("Snake, Water, Gun Game")
window.geometry("1080x720")

#This code creates a label on the Window that greets the user and prompts them to enter their name.
l = Label(window, text = "Welcome to the Snake 🐍 Water 💧 Gun 🔫 Game!\nPlease enter your name below:")
l.config(font =("San Francisco", 40,"bold"))
l.pack()

#This code intitalizes a text entry box in which the font is San Francisco, Apple's default font.
entry = Entry()
entry.config(font=('San Francisco',20))
entry.config(bg = "#000000")
entry.pack()

#This function saves the player name entered through the entry widget, disables the text box, and then proceeds to the game portion of the code.
def submit():
    globals()["playername"]=entry.get()
    entry.config(state=DISABLED)
    gameCode()

#This function disables the button to make sure it isn't pressed again.
def disable():
    ConfirmName.config(state=DISABLED)

#I used a lambda in order to call both functions for the command as it was important to both disable the text box and submit button but also proceed on to the actual code.
ConfirmName = Button(window, text="Submit", command=lambda: [submit(), disable()])
ConfirmName.pack(side = TOP, pady=10)


#The global variables of wins, losses, and draws are defined here.
wins, losses, draws = 0, 0, 0

def gameCode():
    # Score & Data
    results = pd.DataFrame(columns=["Player", "Computer", "Result"])

    #This function attempts to open the image and resize it to dimensions of 150x150 and return nothing if an error is caught.
    def load_image(name, size=(150,150)):
        try:
            img=Image.open(f"{name}.png").resize(size)
            return ImageTk.PhotoImage(img)
        except:
            return None

    #This loads the resized images/emojis from the load_image function into the variables.
    snake_image = load_image("Snake emoji")
    water_image = load_image("Water emoji")
    gun_image = load_image("Watergun emoji")

    img_dict={
        "Snake":snake_image,
        "Water":water_image,
        "Gun":gun_image
    }


    #Creates the corresponding labels for the name of the game, move of the player, as well as the wins, losses, and draws!
    label_title = Label(window, text="Snake Water Gun", font=("San Francisco", 18, "bold"))
    label_title.pack(pady=10)

    preview_image = Label(window)
    preview_image.pack(pady=10)

    label_result = Label(window, text=f"Choose your move, {playername}!", font=("San Francisco", 14))
    label_result.pack(pady=10)

    label_score = Label(window, text="Wins: 0 | Losses: 0 | Draws: 0", font=("San Francisco", 12))
    label_score.pack(pady=10)
    preview_image.config




    #This code consists of the logic for the game.
    def play(player_choice):

        global wins, losses, draws 

        options = ["Snake", "Water", "Gun"]
        #The computer's choice is automatically chosen with the choice method from the random library that we imported at the top.
        computer_choice = choice(options)

        if(player_choice == computer_choice):
            draws+=1
            result = "Draw"
        elif(player_choice=="Snake" and computer_choice=="Water"
            or player_choice=="Water" and computer_choice=="Gun"
            or player_choice=="Gun" and computer_choice=="Snake"):
            wins+=1
            result = "Win"
        else:
            losses+=1
            result = "Loss"

        preview_image.config(image=img_dict[player_choice])
        label_result.config(text=f"You: {player_choice} | Computer: {computer_choice}\nResult: {result}")
        label_score.config(text=f"Wins: {wins} | Losses: {losses} | Draws: {draws}")


    # Buttons with images.
    btn_frame = Frame(window)
    btn_frame.pack(pady=10)

    Button(btn_frame, image=snake_image, command=lambda: play("Snake")).grid(row=0, column=0, padx=10)
    Button(btn_frame, image=water_image, command=lambda: play("Water")).grid(row=0, column=1, padx=10)
    Button(btn_frame, image=gun_image, command=lambda: play("Gun")).grid(row=0, column=2, padx=10)


window.mainloop()
