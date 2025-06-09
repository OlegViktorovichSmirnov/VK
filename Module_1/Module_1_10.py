# Задание!
# Необходимо написать программу, которая будет считывать со стандартного ввода строку. Нужно
# разбить строку на слова, словом будем считать последовательность символов отличных от
# пробелов (то есть знаки пунктуации будут входить в слова). Далее нужно посчитать сколько
# каждое слово встречалось в тексте и вывести наиболее часто слово и сколько оно встретилось.
# Все слова нужно также приводить к нижнему регистру при подсчете. Гарантируется, что в
# тексте самое частое слово – единственное.

import  string
print(f"****Start of input***")
line = input("")
print(f"******End of input***")
words = []
current_word = ""
for char in line:
    if char.isalnum():
        current_word += char
    elif current_word:
        words.append(current_word)
        current_word = ""
if current_word:
    words.append(current_word)
word_counts = {}
for word in words:
    word = word.lower()
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1
most_common_word = ""
most_common_count = 0
for word, count in word_counts.items():
    if count > most_common_count:
        most_common_word = word
        most_common_count = count

print(f"*****-----------*****")
print(f"***Start of Result***")
print(f"Самое повторяемое слово: {most_common_word}, Количество повторений: {most_common_count}")
print(f"*****End of Result***")