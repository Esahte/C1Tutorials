import random

# Computer generates random number to sum
num_1 = random.randint(1, 99)
num_2 = random.randint(1, 99)
# Prompt user to enter answer
answer = int(input('What is ' + str(num_1) + ' + ' + str(num_2) + '?: '))
# Generate if answer is true of false
if answer == num_1 + num_2:
    print('true')
else:
    print('false')
# print(num_1 + num_2 == answer)
