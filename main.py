from art import logo, vs
from replit import clear
from game_data import data
import random

# Display art
print(logo)
score = 0
# make the game repeatable.
game_should_continue = True
choiceB = random.choice(data)
while game_should_continue:
    def format_data(choice):
        """ format the account data into a printable format"""
        choice_name = choice['name']
        choice_description = choice['description']
        choice_country = choice['country']
        return f"{choice_name}, {choice_description}, from {choice_country} "


    def check_answer(guess, follower_a, follower_b):
        """ use if statement to check if user is correct"""
        if follower_a > follower_b:
            return guess == "a"
        else:
            return guess == "b"


    # Generate a random account for game_data
    # making account at position B the next account at position A
    choiceA = choiceB
    choiceB = random.choice(data)
    if choiceA == choiceB:
        choiceB = random.choice(data)

    print(f"Compare A : {format_data(choiceA)}")

    print(vs)

    print(f"Against B: {format_data(choiceB)} ")
    # ask the user for a guess
    user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Check  if user is correct
    # get follower count for each account
    choiceA_count = choiceA['follower_count']
    choiceB_count = choiceB['follower_count']
    is_correct = check_answer(user_choice, choiceA_count, choiceB_count)
    # clear the screen between round.
    clear()
    print(logo)
    # give user feedback on their guess
    # score keeping
    if is_correct:
        score += 1
        print(f"You are right! current score: {score}")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong! final score: {score}")
