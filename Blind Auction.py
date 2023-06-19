import os 

bidders ={}
max =0
winner =""
another_bidder =True

while another_bidder:
  new_bidder =input("What is your name?\n")
  bidders[new_bidder] =int(input("What is your bid?\n$"))
  if max <bidders[new_bidder]:
    winner =new_bidder
    max =bidders[new_bidder]

  answer =input("Are there any other bidders? Please type Yes or No\n")
  os.system('clear')
  answer =answer.lower()
  if answer =='no':
    another_bidder =False

print(f"The winner is {winner} with a bid of ${max}.")