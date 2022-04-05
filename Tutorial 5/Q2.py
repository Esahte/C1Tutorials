# Prompt user to enter a saving amount
sa = float(input('Enter saving amount: '))
mi = 0.00417
# m = months
m1 = (sa * (1 + mi))
m2 = ((sa + m1) * (1 + mi))
m3 = ((sa + m2) * (1 + mi))
m4 = ((sa + m3) * (1 + mi))
m5 = ((sa + m4) * (1 + mi))
m6 = ((sa + m5) * (1 + mi))
print(int(m3*1000)/1000)
