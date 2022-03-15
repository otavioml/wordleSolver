import random

with open('data/words.txt') as f:
    five_letter_word_list = f.read().splitlines()

print("0 is for nonexistent\n1 is for correct letter, but in the wrong place\n2 is for correct letter at the correct place")

while len(five_letter_word_list) != 1:

    guess = input("Enter your guess: ")
    status_letters = input("Enter the letters status: ")

    nonexistent_letters = []
    semi_correct_letters = []
    correct_letters = []


    for i in range(5):
        if (status_letters[i] == '0'):
            nonexistent_letters.append(guess[i])
        elif (status_letters[i] == '1'):
            semi_correct_letters.append((guess[i], i))
        elif (status_letters[i] == '2'):
            correct_letters.append((guess[i], i))

    it = 0

    while it < len(five_letter_word_list):

        leave = False

        current_word = five_letter_word_list[it].lower()

        #if the word contains the nonexistent letter, remove from list
        for nl in nonexistent_letters:
            if (nl in current_word):
                five_letter_word_list.pop(it)
                it -= 1
                leave = True
                break


        #if the word does not contains existent letter or contains it in the wrong place, remove from list
        if (not leave):
            for scl in semi_correct_letters:
                if (not (scl[0] in current_word)):
                    five_letter_word_list.pop(it)
                    it -= 1
                    leave = True
                    break
                else:
                    if (current_word[scl[1]] == scl[0]):
                        five_letter_word_list.pop(it)
                        it -= 1
                        leave = True
                        break

        #if the word does not contains the correct letter at a certain place, remove from list
        if (not leave):
            for cl in correct_letters:
                if (current_word[cl[1]] != cl[0]):
                    five_letter_word_list.pop(it)
                    it -= 1
                    leave = True
                    break

        it += 1

    suggestions_size = min(len(five_letter_word_list), 10)

    print("Sugestions: ", random.sample(five_letter_word_list, suggestions_size))
    print(len(five_letter_word_list))