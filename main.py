row = int(input(f'Enter takes any number: '))

# Print the upper half of the pattern
for i in range(0, row):
    for j in range(i):
        print('*', end='')
    print()

# Print the lower half of the pattern
for k in range(row, 0, -1):
    for l in range(k):
        print('*', end='')
    print()
