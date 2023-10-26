# Import Random Module
import random

# ASCII art for rock, paper and scissors

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Welcome message
print("Welcome to the Rock, Paper, Scissors game!")

# Choice naming
selection = [rock, paper, scissors]
selection_name = ["Rock", "Paper", "Scissors"]

# User input
user_selection = ["r", "p", "s"]
user_input = input("Enter 'R' for rock, 'P' for paper, or 'S' for scissors: ")
user_input = user_input.lower()
user_choice = selection_name[user_selection.index(user_input)]

# computer choice
computer_int = random.randint(0, 2)
computer_choice = selection_name[computer_int]

# Displaying choices
print(f"Computer chose: {computer_choice}")
print(selection[computer_int])
print("\n\n")
print(f"You chose: {user_choice}")
print(selection[user_selection.index(user_input)])

# Logic to see who wins
if user_choice == computer_choice:
    print("It's a Draw!")
elif user_choice == "Rock" and computer_choice == "Scissors" or user_choice == "Scissors" and computer_choice == "Paper" or user_choice == "Paper" and computer_choice == "Rock":
    print("You won!")
else:
    print("You lose")

