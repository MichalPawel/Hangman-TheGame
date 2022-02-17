import sys
import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


no_of_tries = 5
word = 'truck'
used_letters = []

user_word = []
user_word_string = " "


def find_indexes(word, letter):
    indexes = []

    for index, letter_in_word in enumerate(word):
        if letter == letter_in_word:
            indexes.append(index)
    return indexes


for _ in word:
    user_word.append("_")

print(user_word_string.join(user_word))
while True:
    letter = input('Type a letter: ')
    used_letters.append(letter)
    cls()
    print("Letters used: " + str(used_letters))
    found_indexes = find_indexes(word, letter)
    if len(found_indexes) < 1:
        no_of_tries -= 1
        print()
        print('There is no letter "' + letter + '" in the search word.')
        print(str(no_of_tries) + " attempts remaining")
        print()
        print(user_word_string.join(user_word))
        if no_of_tries == 0:
            print('Game over :(')
            sys.exit(0)
    elif len(found_indexes) > 0:
        for index in found_indexes:
            user_word[index] = word[index]

        print()
        print(user_word_string.join(user_word))
        if user_word.count("_") == 0:
            print('You Win!')
            sys.exit(0)
