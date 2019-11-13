####################
### HANGMAN GAME ###
####################

# IMPORT LIBRARY'S
import random
import os
from re import finditer

## SET SOME VALUES
# List of secret words to guess
random_words = ['elefante','barco','edificio','italia','loro','urraca','mono','automovil','esperanza']
# Random pick of secret word
secret_word = random.choice(random_words)

# Init variables
game_on=True
attempts=6
guessed_letters = []
attempted_letters =[]

# FUNCTIONS!
# Hangman drawing function
def stage(attempts):
    hangman_draw=[' _______',
                '|      |',
                ['|      ','|      O'],
                ['|     ','|     /','|     /|','|     /|\\'],
                ['|      ','|     /','|     / \\']]
    stage={6:[0,0,0],5:[1,0,0],4:[1,1,0],3:[1,2,0],2:[1,3,0],1:[1,3,1],0:[1,3,2]}
    a,b,c = stage.get(attempts,[0,0,0])
    print(hangman_draw[0],'\n',hangman_draw[1],'\n',hangman_draw[2][a],'\n',hangman_draw[3][b],'\n',hangman_draw[4][c]),
    print()

    print('SECRET WORD: ',end='',flush=True)
    for i in range(len(secret_word)):
        if i in guessed_letters:
            print(secret_word[i]+' ',end='',flush=True)
        else:
            print('_'+' ',end='',flush=True)
    print()

# Clear screen function
clear = lambda: os.system('cls')

## GAME LOGIC
print('WELCOME TO HANGMANE!')
print('\n')
print('LET´S PLAY!')

# Draw the starting stage of hangman
stage(attempts)

# While word not guessed or number of attempts not 0
while game_on :
    # Init repetead letter
    repeated=False

    # Request a letter
    letter_guess = input('Give a word to guess: ')

    # Clear screen to start drawing the hangman
    clear()

    # Check if letter is repetead
    if letter_guess in attempted_letters:
        print('>> REPEATED LETTER <<')
        repeated=True
    else:
        # if not repetead add to attempted letters list
        attempted_letters.append(letter_guess)

    # If letter not repetead, check if is in word
    if not repeated :
        if letter_guess in secret_word :
            # If in word let it know
            print(('The letter {} is in the word!').format(letter_guess))
            # And save at what index was founded
            for m in finditer(letter_guess,secret_word):
                guessed_letters.append(m.start())
        else:
            # if not in word let it know
            print(('The letter {} is NOT in the word!').format(letter_guess))
            # Decrease counter of attempts
            attempts -= 1

    # Show number of attempts left
    print(('You have {} attempts left').format(attempts))

    # Draw hangmand and show how the word guessing goes
    stage(attempts)

    # Check if still remain attempts
    if attempts < 1:
        game_on=False
        print('GAME OVER!')
        print('The word was:',secret_word)

    # Check if the word was guessed
    if len(secret_word) == len(guessed_letters):
        game_on=False
        print('YOU WIN!')
