subtotal = int(input('Enter subtotal: '))
gratuity = float(input('Enter gratuity rate: '))
gratuity_rate = (gratuity/100) * subtotal
print('gratuity=', gratuity_rate)
print('total= ', gratuity_rate + subtotal)