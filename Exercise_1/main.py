"""Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
Поскольку разобраться в его кричалках не настолько просто, насколько легко
он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть,
если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
Фраза может состоять из одного слова, если во фразе несколько слов, то они
разделяются дефисами. Фразы отделяются друг от друга пробелами.
Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите
“Парам пам-пам”, если с ритмом все в порядке и “Пам парам”,
если с ритмом все не в порядке"""


import sys


class PhrasesException(Exception):
    pass


lyrics = input("Enter your lyrics: ").lower()
vowel_letters = ['а', 'о', 'э', 'е', 'и', 'ы', 'у', 'ё', 'ю', 'я']


def count_vowels(lyr, vowels):
    count_vowels = []
    try:
        phrases = lyr.split()
        if len(phrases) < 2:
            raise PhrasesException("You must enter at least 2 phrases!")
    except PhrasesException as ex:
        print(ex)
        sys.exit()
    for i in phrases:
        count_vowels.append(len([x for x in i if x in vowels]))
    if count_vowels.count(count_vowels[0]) == len(count_vowels):
        return "Парам пам-пам"
    else:
        return "Пам парам"


result = count_vowels(lyrics, vowel_letters)
print(result)
