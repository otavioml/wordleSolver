from nltk.corpus import words
word_list = words.words()

five_letter_word_list = []
for word in word_list:
    if (len(word) == 5):
        five_letter_word_list.append(word)

print(len(five_letter_word_list))

five_letter_word_list = ['andre', 'otavi', 'aaaaa', 'abcde', 'abcdb', 'otbvi']

# print("0 is for nonexistent\n1 is for correct letter, but in the wrong place\n2 is for correct letter at the correct place")
guess = input("Enter your guess: ")
status_letters = input("Enter the letters status: ")


nonexistent_letters = []
semi_correct_letters = []
correct_letters = []

leave = False

for i in range(5):
    if (status_letters[i] == '0'):
        nonexistent_letters.append(guess[i])
    elif (status_letters[i] == '1'):
        semi_correct_letters.append((guess[i], i))
    elif (status_letters[i] == '2'):
        correct_letters.append((guess[i], i))

for w in five_letter_word_list:

    #if the word contains the nonexistent letter, remove from list
    for nl in nonexistent_letters:
        print("Testing word", w, "with letter ", nl)
        if (nl in w):
            five_letter_word_list.remove(w)
            print(w, " contains ", nl, ". Removed from list.")
            leave = True

    # #if the word does not contains existent letter or contains it in the wrong place, remove from list
    # if (not leave):
    #     for scl in semi_correct_letters:
    #         if (not (scl[0] in word)):
    #             five_letter_word_list.remove(word)
    #             leave = True
    #             break

    #         else:
    #             if (word[scl[1]] == scl[0]):
    #                 five_letter_word_list.remove(word)
    #                 leave = True
    #                 break

    # #if the word does not contains the correct letter at a certain place, remove from list
    # if (not leave):
    #     for cl in correct_letters:
    #         if (word[cl[1]] != cl[0]):
    #             five_letter_word_list.remove(word)
    #             leave = True
    #             break

print(five_letter_word_list[:10])
print(len(five_letter_word_list))