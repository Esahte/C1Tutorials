yr = int(input('enter year: '))
tu_c = 10000
inc_p = 0.05
# fixed_tc = 10000
for x in range(0, yr):
    tu_c = (inc_p * tu_c) + tu_c
    # tu_c = (inc_p * fixed_tc) + tu_c
    x += 1
print(round(tu_c, 2))
