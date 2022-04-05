sa = float(input('Enter saving amount: '))
mi = int(input('monthly interest: '))
m = int(input('months: '))
x = mi / 1200
j = 1
m1 = 0
while j <= m:
    m1 = ((sa + m1) * (1 + x))
    # print(round(m1, 3))
    j += 1
print(round(m1, 3))
# sounds nice


