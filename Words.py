# Задание!
# Необходимо будет написать программу, которая будет считывать со стандартного ввода строку
# и выводить на стандартный вывод является ли строка “правильной”. Строка считается правильной,
# если в ней есть латинская буква “a” или “o”, но нет букв “i” и “e”. Строка содержит только
# латинские буквы в нижнем регистре.

try:
    while True:
        word = input()
        if (('a' in word or 'o' in word) and not 'i' in word and not 'e' in word):
            print(True)
        else:
            print(False)
except EOFError:
    pass
