#import the requirement libraries
import random

# write 'Hello World' in the console
print('Hello World')

# define two global integer variables gamer_score and system_score
gamer_score = 0
system_score = 0

# generate a list of strings: rock, paper, scissors
rock_paper_scissors_options = ['rock', 'paper', 'scissors']

# generate a function to accept two strings: gamer_input and system_input 
# if the gamer_input is rock and system_input is scissors, gamer_score is incremented by 1
# if the gamer_input is rock and system_input is paper, system_score is incremented by 1
# if the gamer_input is scissors and system_input is paper, gamer_score is incremented by 1
# if the gamer_input is scissors and system_input is rock, system_score is incremented by 1
# if the gamer_input is paper and system_input is rock, gamer_score is incremented by 1
# if the gamer_input is paper and system_input is scissors, system_score is incremented by 1
# if the gamer_input is equal to system_input, no score is incremented

def rock_paper_scissors(gamer_input, system_input):
    global gamer_score
    global system_score
    if gamer_input == 'rock' and system_input == 'scissors':
        gamer_score += 1
    elif gamer_input == 'rock' and system_input == 'paper':
        system_score += 1
    elif gamer_input == 'scissors' and system_input == 'paper':
        gamer_score += 1
    elif gamer_input == 'scissors' and system_input == 'rock':
        system_score += 1
    elif gamer_input == 'paper' and system_input == 'rock':
        gamer_score += 1
    elif gamer_input == 'paper' and system_input == 'scissors':
        system_score += 1
    else:
        pass

# generate a function to accept string from user and assign the value to gamer_input
# the input string must be present in the list rock_paper_scissors
def gamer_input():
    gamer_input = input('Enter rock, paper or scissors: ')
    if gamer_input in rock_paper_scissors_options:
        return gamer_input
    else:
        print('Invalid input. Please enter rock, paper or scissors')
        gamer_input()

# generate a random string from the list and assign it to system_input
def system_input():
    system_input = random.choice(rock_paper_scissors_options)
    return system_input

# generate a function to print the gamer_score and system_score
def print_score():
    print('Gamer Score: ', gamer_score)
    print('System Score: ', system_score)

# generate a function to accept the number of rounds from the user
# the number of rounds must be an integer
def number_of_rounds():
    try:
        rounds = int(input('Enter the number of rounds: '))
        return rounds
    except ValueError:
        print('Invalid input. Please enter a number')
        number_of_rounds()

# generate a function to play the game
# the function accepts the number of rounds from the user
# the function runs the game for the number of rounds
# the function prints the scores after each round
def play_game():
    rounds = number_of_rounds()
    for i in range(rounds):
        system = system_input()
        gamer = gamer_input()
        rock_paper_scissors(gamer, system)
        print_score()

play_game()

#fix the bug in the code
# UnboundLocalError: cannot access local variable 'system_score' where it is not associated with a value
