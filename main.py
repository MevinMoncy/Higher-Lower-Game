#Author: Mevin Moncy

from game_data import data
from art import logo, vs
import random

def format_data(compare):
  """Formats the data into printable format"""
  compare_name = compare['name']
  compare_descr = compare['description']
  compare_country = compare['country']
  return f" {compare_name}, a {compare_descr}, from {compare_country} "

def check_answer(guess, a_followers, b_followers):
  """Takes the user guess and follower counts and returns if they got it right"""
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"

# Display art
print(logo)
score = 0
game_should_continue = True
compare2 = random.choice(data)

# Make the game repeatable
while game_should_continue:
  # Generate a random account from the game data
  compare1 = compare2
  compare2 = random.choice(data)
  while compare1 == compare2:
    compare2 = random.choice(data)

  # Format account data into printable format
  print(f"Compare A: {format_data(compare1)}")
  print(vs)
  print(f"Against B: {format_data(compare2)}")

  # Ask users for a guess
  guess = input("Who has more followers? Type 'A' or 'B': ").lower()

  # Check if the user's answer is correct or not
  a_follower_count = compare1['follower_count']
  b_follower_count = compare2['follower_count']
  is_correct = check_answer(guess, a_follower_count, b_follower_count)

  # Clear the screen between rounds
  # Clearing the screen was removed since 'replit' is not available

  print(logo)

  # Give user feedback on their answer and keep score
  if is_correct:
    score += 1
    print(f"You're correct! Current score: {score}.")
  else:
    game_should_continue = False
    print(f"You're wrong. Final score: {score}.")
