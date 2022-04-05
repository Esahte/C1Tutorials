# Prompt user to enter 3 different numbers
a, b, c = eval(input('Enter any real number: '))
# discriminant(d)
d = (b * b) - (4 * (a * c))  # formula to find discriminant
# Program computes quadratic formula
r_1 = (-b + (d ** 0.5)) / (2 * a)
r_2 = (-b - (d ** 0.5)) / (2 * a)
# display results
if d == 0:
    print('The root is', r_1)
elif d > 0:
    print('The roots are', r_1, 'and', r_2)
else:
    print('The equation has no real roots')

# examples:
# 1, 10, 25
# 1, -2, -35
# 2, -7, 4
# -2, 3, -3
