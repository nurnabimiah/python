n = int(input('Enter the input number:  '))
d1, d2 = 0, 1
print('Fibo series: ', d1, d2,end= ' ')

# loop
for i in range(2, n):
    fibo_number = d1 + d2
    print(fibo_number, end=" ")
    d1 = d2
    d2 = fibo_number




