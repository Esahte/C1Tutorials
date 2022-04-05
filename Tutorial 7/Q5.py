import random

cf = int(input('enter how many times to coin flip: '))
heads = 0
tails = 0
for x in range(0, cf):
    flip = random.randint(0, 1)
    if flip == 1:
        heads += 1
    else:
        tails += 1
    x += 1

print('heads = ', heads)
print('tails = ', tails)
