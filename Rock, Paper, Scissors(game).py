import random

rock = """
   _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

"""

scissors = """
     _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

"""

print("Welcome to the Rock, Paper, Scissors game:")
rules = input("Press Enter to continue or type (Help) for the rules: ").lower()
if rules == 'help':
    print("""
             ********* RULES *********
        1) You choose and the computer chooses
        2) Rock smashes Scissors -> Rock wins
        3) Scissors cut Paper -> Scissors win
        4) Paper covers Rock -> Paper wins
 """)
    
  # User Choice  

user_choice = input("Enter your choice (rock, paper, scissors): ").lower()

if user_choice == 'rock':
    print(f"You chose:\n\n{rock}")
elif user_choice == 'paper':
    print(f"You chose:\n\n{paper}")
elif user_choice == 'scissors':
    print(f"You chose:\n\n{scissors}")
else:
    print("Invalid choice. Please run the program again and choose rock, paper, or scissors.")
    exit()

 # Computer Choice

computer_choice = random.choice(['rock', 'paper', 'scissors'])

if computer_choice == 'rock':
    print(f"computer chose:\n\n{rock}")
elif computer_choice == 'paper':
    print(f"computer chose:\n\n{paper}")
else:
    print(f"computer chose:\n\n{scissors}")

# Determine the winner

if user_choice == computer_choice:
    print("It's a tie!")
elif (
    (user_choice == 'rock'  and  computer_choice == 'scissors')
 or (user_choice == 'paper'  and  computer_choice == 'rock')
 or (user_choice == 'scissors'  and  computer_choice == 'paper')
):
    print(f"You win! {user_choice} beats {computer_choice}.")
else:
    print(f"You lose! {computer_choice} beats {user_choice}.")


