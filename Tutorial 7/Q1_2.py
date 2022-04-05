for x in range(1, 6 + 1):
    for j in range(1, x + 1):
        print(j, end=" ")
    print()

for x in range(1, 6 + 1):
    for j in range(1, 7 - x + 1):
        print(j, end=" ")
    print()

for x in range(1, 6 + 1):
    # Print leading space
    for j in range(6 - x, 0, -1):
        print("  ", end="")
    for j in range(x, 0, -1):
        print(j, end=" ")
    print()