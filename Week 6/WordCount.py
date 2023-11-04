#outside loop

words_list = []
count = 0

while len(words_list) < 5:
    word = input("Enter word (x to exit): ")

    if word == "x":
        break
    if word in words_list:
        print(f"{word} has already been entered.")
        continue
    words_list.append(word)
    count += len(word)

print("You words are: ", words_list)
print("The number of letters in these words is", count)
