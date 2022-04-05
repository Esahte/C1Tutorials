# Prompt user to enter 3 random no.
a, b, c, = eval(input('Enter three random numbers: '))
# Add the perimeter
P = a + b + c
# Generate answer
if a + b < c:
    print('The input is invalid')
elif b + c < a:
    print('The input is invalid')
elif a + c < b:
    print('The input is invalid')
else:
    print('The perimeter is', P)
