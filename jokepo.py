from tkinter import *
from PIL import ImageTk, Image
import random

root = Tk()

root.title("Rock Paper Scissors")

root.geometry("800x680")
canvas = Canvas(root, width=800, height=680)
canvas.grid(row=0, column=0)

l1 = Label(root, text="Player", font=("Algerian", 25))
l2 = Label(root, text="Computer", font=("Algerian", 25))
l3 = Label(root, text="Vs", font=("Algerian", 40))

l1.place(x=80, y=20)
l2.place(x=560, y=20)
l3.place(x=370, y=230)

#default image
img_p = Image.open("default.jpg")
img_p = img_p.resize((300, 300))

img_c = img_p.transpose(Image.FLIP_LEFT_RIGHT)

img_p = ImageTk.PhotoImage(img_p)
img_c = ImageTk.PhotoImage(img_c)

#rock image
rock_p = Image.open("rock.jpg")
rock_p = rock_p.resize((300, 300))

rock_c = rock_p.transpose(Image.FLIP_LEFT_RIGHT)

rock_p = ImageTk.PhotoImage(rock_p)
rock_c = ImageTk.PhotoImage(rock_c)

#paper image
paper_p = Image.open("paper.jpg")
paper_p = paper_p.resize((300, 300))

paper_c = paper_p.transpose(Image.FLIP_LEFT_RIGHT)

paper_p = ImageTk.PhotoImage(paper_p)
paper_c = ImageTk.PhotoImage(paper_c)

#scissor image
scissor_p = Image.open("scissor.jpg")
scissor_p = scissor_p.resize((300, 300))

scissor_c = scissor_p.transpose(Image.FLIP_LEFT_RIGHT)

scissor_p = ImageTk.PhotoImage(scissor_p)
scissor_c = ImageTk.PhotoImage(scissor_c)

#selection image
img_s = Image.open("select.jpg")
img_s = img_s.resize((300, 130))
img_s = ImageTk.PhotoImage(img_s)

canvas.create_image(0, 100, anchor=NW, image=img_p)
canvas.create_image(500, 100, anchor=NW, image=img_c)
canvas.create_image(0, 400, anchor=NW, image=img_s)
canvas.create_image(500, 400, anchor=NW, image=img_s)

#game function
while True:
    user_choice = input("Choose between: rock, paper, or scissors\n")
    possible_choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(possible_choices)

    print(f"\nYou chose {user_choice}, computer chose {computer_choice}.\n")

    if user_choice == computer_choice:
        print(f"Both players selected {user_choice}. It's a TIE")
    elif user_choice == "rock":
        if computer_choice == "scissors":
            print("Rock smashes scissors! You win! :)")
        else:
            print("Paper cover rock! You lose. :(")
    elif user_choice == "paper":
        if computer_choice == "rock":
            print("Paper cover rock! You win. :)")
        else:
            print("Scissors cut paper! You lose :(")
    elif user_choice == "scissors":
        if computer_choice == "paper":
            print("Scissors cut paper. You win!")
        else:
            print("Rock smashes scissors! You lose!")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
                    

