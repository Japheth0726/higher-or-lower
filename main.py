# Display art
from art import logo, vs
from game_data import data
import random


def format_data(account):
    """Takes the account data and return printable format"""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

# Use if statement to check if user is correct
def check_answer(user_guess, a_followers_count, b_followers_count):
    """Takes user's guess against followers count and returns if they got it right or not"""
    if a_followers_count > b_followers_count:
        return user_guess == "a"
    else:
        return user_guess == "b"
    

print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

# Make the game repeatable
while game_should_continue:
    # Generate a random account from the game data
    
    # Making the account at position b become the account at position A
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)
        

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")
        
        

    # Ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B'. ").lower()
    
    # clear the screen
    print("\n" * 20)
    print(logo)



    ## Get follower count of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    # check if guess is correct
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # score keeping
    # Give user feedback on their guess
    if is_correct:
        score += 1
        print(f"You are right! Current score: {score}")
    else:
        print(f"You are wrong! Final score: {score}")
        print(f"{account_a['name']} has {a_follower_count}m followers while,")
        print(f"{account_b['name']} has {b_follower_count}m followers.")
        game_should_continue = False



 

    