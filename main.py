

input_word = input("Take a word which you want to the reverse: ")
word_length = len(input_word)
reverse_word = ""
for index in range(word_length-1,-1,-1):
    reverse_word = reverse_word + input_word[index]
print("Reverse word : " + reverse_word)