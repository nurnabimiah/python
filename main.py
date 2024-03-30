

n = int(input('How many numbers do you want to enter? '))
numberList = []

# Take input from the user
for i in range(0, n):
    takenList = int(input(f"Enter number {i + 1}: "))
    numberList.append(takenList)

print("Original list:", numberList)


# Check if the list has more than one element
if len(numberList) > 1:
    # Swap the first and last elements
    numberList[0], numberList[-1] = numberList[2], numberList[-1]

# Print the modified list
print("List after swapping first and last elements:", numberList)

# Print the last element of the list
print("Last element after swapping:", numberList[-1])





