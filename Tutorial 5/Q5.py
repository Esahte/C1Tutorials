# User will be prompted to enter a the minutes
mins = int(input('Enter the minutes: '))
# This will calculate the total amount of days in minutes
A = (mins/1440)
# This will calculate the maximum amount of years
B = int(A/365)
# This will calculate the remaining days for the minutes
C = int(A % 365)
print('Maximum number of years: ', B)
print('Remaining days: ', C)
