from nltk.corpus import words
word_list = words.words()

five_letter_word_list = []
for word in word_list:
    if (len(word) == 5):
        five_letter_word_list.append(word)

sourceFile = open('words.txt', 'w')

for word in five_letter_word_list:
    print(word, file = sourceFile)

sourceFile.close()