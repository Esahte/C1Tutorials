n = 6
for x in range(n):
    for j in range(x + 1):
        print(j+1, end=' ')
    print()
print()
for x in range(n):
    for j in range(n - x - 1):
        print(' ', end=' ')
    for j in range(x, -1, -1):
        print(j+1, end=' ')
    print()
print()
for x in range(n):
    for j in range(6 - x):
        print(j+1, end=' ')
    print()
