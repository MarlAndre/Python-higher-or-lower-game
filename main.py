from art import logo, vs
from game_data import data
from replit import clear
import random

# Random account
def random_account():
  return random.choice(data)

# Format the data into readable format
def format(data):
  name = data["name"]
  description = data["description"]
  country = data["country"]
  return f"{name}, a {description} from {country}"

## Use if statement to check if user is correct
def check_guess(guess, a_followers, b_followers):
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"


def game():
  print(logo)
  continue_game = True
  score = 0
  
  while continue_game:
    account_a = random_account()
    account_b = random_account()
  
    # Make sure to not get the same account twice
    if account_a == account_b:
      account_b = random_account()
  
    print(f"Compare A: {format(account_a)}")
    print(vs)
    print(f"Against B: {format(account_b)}")
    
    # Ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
  
    ## Get follower count for each account
    a_followers = account_a["follower_count"]
    b_followers = account_b["follower_count"]
    
    # Check if correct
    is_correct = check_guess(guess, a_followers, b_followers)
    
    clear()
    print(logo)
    if is_correct:
      score += 1
      print(f"You're right. Your score: {score}.")
    else:
      continue_game = False
      print(f"You're wrong. Final score: {score}")
    

game()