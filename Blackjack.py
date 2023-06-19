import random
import os

def deal_card():
  """Returns a random card from the deck."""
  cards =[11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card =random.choice(cards)
  return card
  
def calculate_score(cards):
  """Takes a list of cards and returns the score calculated from the sum of cards"""
  if sum(cards) >21 and 11 in cards:
    cards.remove(11)
    cards.append(1)
    
  if sum(cards) ==21 and len(cards) ==2:
    return 0
  return sum(cards)

def compare(user_score, computer_score):
  if user_score ==computer_score:
    return "Draw"
  elif computer_score ==0:
    return "You lost, opponent has Blackjack."
  elif user_score ==0:
    return "You won, you have a Blackjack."
  elif user_score >21:
    return "You lost, you went over."
  elif computer_score >21:
    return "You won, opponent went over."
  elif user_score >computer_score:
    return "You won, you have a higher score."
  else:
    return "You lost, opponent has a higher score."


play_again =True

while play_again:
  computer_cards =[]
  user_cards =[]
  game_over =False
  
  for i in range(0,2):
    computer_cards.append(deal_card())
    user_cards.append(deal_card())
  
  game_over =False
  while not game_over:
    """USER WHILE LOOP"""
    user_score =calculate_score(user_cards)
    computer_score =calculate_score(computer_cards)
      
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first cards: {computer_cards[0]}")
    
    if user_score ==0 or computer_score ==0 or user_score >21:
      game_over =True
    else:
      draw_again =input("Type 'y' to get another card, type 'n' to pass: ")
      if draw_again =='y':
        user_cards.append(deal_card())
      if draw_again =='n':
        game_over =True
  
  while computer_score !=0 and computer_score <17:
    """COMPUTER WHILE LOOP"""
    computer_cards.append(deal_card())
    computer_score =calculate_score(computer_cards)
  
  print(f"Your final hand: {user_cards}, Your final score: {user_score}")
  print(f"Opponent's final hand: {computer_score}, Opponent's final score: {computer_score}")
  print(compare(user_score, computer_score))

  answer =input("Do you want to play again? Type 'y' or 'n': ")

  if answer =='y':
    play_again =True
    os.system('clear')
  else:
    play_again =False