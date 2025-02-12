#Rock Paper Scissors
import random
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

user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors")
user_choice = int(user_choice)
choices = [rock, paper, scissors]
print("User choice is:\n" + choices[user_choice])

computer_choice = random.randint(0,3)
print("Computer choice is:\n" + choices[computer_choice])

if (user_choice == 0 and computer_choice == 1) or (user_choice == 1 and computer_choice == 2) or (user_choice == 2 and computer_choice == 0):
    print("Computer wins.")
elif (user_choice == 1 and computer_choice == 0) or (user_choice == 2 and computer_choice == 1) or (user_choice == 0 and computer_choice == 2):
    print("User wins.")
else:
    print("It's a draw.")