import random

import sys

# Computer generates random number between 0 and 2
comp_guess = random.randint(0, 2)
# scissor = 0
# rock = 1
# paper = 2
# Prompt player to enter a number
player_guess = int(input('Enter a random word between rock(1), paper(2), and scissor(0): '))
# scissor(0) > paper(2)
# rock(1) > scissor(0)
# paper(2) > rock(1)

if comp_guess == 2:
    if player_guess == 2:
        print('The computer is paper. You are paper too. It is a draw.')
    elif player_guess == 0:
        print('The computer is paper. You are scissor. You won')
    elif player_guess == 1:
        print('The computer is paper. You are rock. The computer won')
elif comp_guess == 1:
    if player_guess == 1:
        print('The computer is rock. You are rock too. It is a draw.')
    elif player_guess == 2:
        print('The computer is rock. You are paper. You won')
    elif player_guess == 0:
        print('The computer is rock. You are scissor. The computer won')
elif comp_guess == 0:
    if player_guess == 0:
        print('The computer is scissor. You are scissor too. It is a draw.')
    elif player_guess == 1:
        print('The computer is scissor. You are rock. You won')
    elif player_guess == 2:
        print('The computer is paper. You are scissor. You won')
else:
    print('Error: invalid number')
    sys.exit()
