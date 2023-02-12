from game_data import data
from art import logo, vs
import random
from replit import clear


def format_data(compare):
  """Formts the data into printable format"""
  compare_name = compare['name']
  compare_descr = compare['description']
  compare_country = compare['country']
  return f" {compare_name}, a {compare_descr}, from {compare_country} "
  
def check_answer(guess, a_followers, b_followers):
  """takes the user guess and follower counts and returns if they got it right"""
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"
  
  

#display art
print(logo)
score = 0
game_should_continue = True
compare2 = random.choice(data)

#Make the game repeatable
while game_should_continue:
  #generate a random account from the game data
  compare1 = compare2
  compare2 = random.choice(data)
  while compare1 == compare2:
    compare2 = random.choice(data)
    
  
  #format account data into printable format
  print(f"Compare A: {format_data(compare1)}")
  
  print(vs)
  
  print(f"Against B: {format_data(compare2)}")
  
  #ask users for a guess
  guess = input("Who has more followers? Type 'A' or 'B': ").lower()
  
  #check users answer is correct or not
  ##Get follower count for each account
  a_follower_count = compare1['follower_count']
  b_follower_count = compare2['follower_count']
  
  is_correct = check_answer(guess, a_follower_count, b_follower_count)
  
  #clear the screen between rounds
  clear()
  print(logo)
  
  #give user feedback on their answer
  # score keep
  if is_correct:
    score += 1
    print(f"You're correct! Current score: {score}.")
    
  else:
    game_should_continue = False
    print(f"you're wrong. Final score: {score}.")
  





