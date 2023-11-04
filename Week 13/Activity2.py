sen = input('Enter a sentence: ')
sen = sen.lower()

letters_dict = {} 

#for loop to add things into dict
for char in sen:
    if char.isalpha():
        if char in letters_dict:
            letters_dict[char] += 1
        else:
            letters_dict[char] = 1

#Loop to print
for things in letters_dict:
    print('{:s} : {:d}'.format(things, letters_dict[char]))
    