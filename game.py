# create a simple rock, paper, scissors game
# provide a welcome message
# get the user's choice
# get the computer's choice
# compare the two choices
# print a message saying who won and the choices made
# ask the user if they want to play again
# say goodbye and end the game
# use one function for the game logic

import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "win"
    else:
        return "lose"

def game():
    print("Welcome to Rock, Paper, Scissors!")
    user_choice = input("Enter rock, paper, or scissors: ")
    computer_choice = get_computer_choice()
    print(f"The computer chose {computer_choice}.")
    result = determine_winner(user_choice, computer_choice)
    if result == "tie":
        print("It's a tie!")
    elif result == "win":
        print("You win!")
    else:
        print("You lose!")
    play_again = input("Do you want to play again? (yes/no) ")
    if play_again == "yes":
        game()
    else:
        print("Goodbye!")

game()