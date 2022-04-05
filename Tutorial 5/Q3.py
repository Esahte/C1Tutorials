# through out this program letter will be used to display certain words
# these word are
# distance = 'd'
# miles per hour = 'mph'
# price per hour = 'pph'
# Prompt user to enter distance
d = float(input('Enter drive distance: '))
# Prompt user to enter miles per gallon
mpg = float(input('Enter miles per gallon: '))
# Prompt user to enter price per gallon
ppg = float(input('Enter price per gallon: '))
print((int(((d/mpg)*ppg)*100))/100)