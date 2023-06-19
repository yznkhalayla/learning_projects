
import random
import os

print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

play_again =True
while play_again:
  difficulty =input("Choose a difficulty: 'easy' or 'hard'\n")
  
  if difficulty =='easy':
    n =10
  elif difficulty =='hard':
    n =5
  
  number =random.randint(1,100)
  while n >0:
    print(f"You have {n} attempts to guess the number.")
    n -=1
    
    guess =int(input("Make a guess: "))
    if guess ==number:
      print("You guessed the number")
      n =-1
    elif guess>number:
      print("Too High.")
    elif number>guess:
      print("Too Low.")
  
  if n ==0:
    print("You lost.")
  
  answer =input("Do you want to play again? Type 'y' or 'n': ")
  if answer =='y':
    play_again =True
    os.system('clear')
  elif answer =='n':
    play_again =False