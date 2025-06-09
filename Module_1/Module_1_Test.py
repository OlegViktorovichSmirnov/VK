# Задание!
# Необходимо написать программу, которая будет принимать на вход строку, разбивать строку
# на слова по пробелу. Далее нужно из всех слов убрать следующие пунктуационные знаки:
# !,.?;:#$%^&*(), а также привести слова к нижнему регистру. В итоге нужно вывести в алфавитном
# порядке слова, которые состоят как минимум из 5 символов, а также имеют как минимум 4
# уникальных символа, и которые встретились в исходном тексте более 2х раз.

import string

# Очистка строки от символов
def clean_word(word):
    return ''.join([char for char in word if char not in string.punctuation])

input_string = input("")

# Разбивка строки на слова, очищение от символов, приведение к нижнему регистру
words = input_string.split()
words = [clean_word(word.lower()) for word in words]

# Сборка слов удовлетворяющих требованиям
accepted_words = {}
for word in words:
    if len(word) >= 5 and len(set(word)) >=4:
        if word in accepted_words:
            accepted_words[word] +=1
        else:
            accepted_words[word] =1

filtered_words = [word for word in accepted_words if accepted_words[word] > 2]

# Сортировка в алфавитном порядке
filtered_words.sort()

for word in filtered_words:
    print(word)