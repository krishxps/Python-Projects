import random as r
import os
logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|    
"""
def play_game():
  _ = os.system("cls")
  print(logo)
  number_to_Guess = r.randint(1,100)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")

  attempt = 0

  level = input("Choose Difficulty : 'Easy' or 'Hard' for easy type 'e' and for Hard type 'h':")
  if level == 'e':
    attempt = 10
  else:
    attempt = 5

  number = False

  while not number:
    print(f"You have {attempt} attemps remaining to guess the number.")
    guess = int(input("Make a Guess: "))
    if attempt <= 1:
      print(f"You Lose Your Guesses are over, actual number was {number_to_Guess}...!")
      number = True
    elif guess == number_to_Guess:
      number = True
      print(f"You got it number was {guess}")
    elif guess > number_to_Guess:
      print("Your Guess is High")
      attempt -= 1
    elif guess < number_to_Guess:
      print("Your Guess is Low")
      attempt -= 1

play_game()
again = input("\nDo you want to play game again? 'y' For Yes and 'n' For NO:")
if again == 'y':
  play_game()
if again == 'n':
    _ = os.system("cls")