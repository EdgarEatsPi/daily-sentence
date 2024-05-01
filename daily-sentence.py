from random import randint, seed
from datetime import date

seed(int(date.today().strftime('%Y%m%d')))

words = open("word-def.txt")

word_def = words.readlines()[randint(0,4840)]

print(word_def)
separator = " "
word = word_def.split(separator, 1)[0]
print("Write 3 sentences that use the word correctly.")
sentence1 = input("Sentence 1: ")
sentence2 = input("Sentence 2: ")
sentence3 = input("Sentence 3: ")
score = 0

if word.lower() in sentence1.lower():
    score += 1
if word.lower() in sentence2.lower():
    score += 1
if word.lower() in sentence3.lower():
    score += 1
print("Your score is", score, ".")
