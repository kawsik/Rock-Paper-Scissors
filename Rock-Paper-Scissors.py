#Here is the code for Rock-Paper-Scissors
import random

print("Welcome to the Rock-Paper-Scissors game!")
choice = input("Would like to play? Type 'Yes' to continue: ").lower()

if choice != "yes":
    quit()

choices = ["rock","paper","scissors"]
user_wins = 0
computer_wins = 0
draws = 0

while True:
    print()
    user_choice = input("Choose between rock, paper and scissors and q to quit: ").lower()
    if user_choice == "q":
        break
    computer_choice = choices[random.randint(0,2)]
    
    if user_choice == "rock" and computer_choice == "scissors":
        print("You Win!")
        user_wins += 1
    elif user_choice == "paper" and computer_choice == "rock":
        print("You Win!")
        user_wins += 1
    elif user_choice == "scissors" and computer_choice == "paper":
        print("You Win!")
        user_wins += 1
    elif user_choice == computer_choice:
        print("You Drew")
        draws += 1
    else:
        print("You Lost")
        computer_wins += 1

print(f"You have won {user_wins} times against computer.")
print(f"Computers has won {computer_wins} times against you.")
print(f"There were {draws} draws.")
