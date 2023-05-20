# Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает,
# Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов
# (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
# Фразы отделяются друг от друга пробелами.
# Стихотворение Винни-Пух вбивает в программу с клавиатуры.
# В ответе напишите "Парам пам-пам", если с ритмом все в порядке и
# "Пам парам", если с ритмом все не в порядке.

# Ввод:
# пара-ра-рам рам-пам-папам па-ра-па-дам

# Вывод:
# Парам пам-пам

# def rhythm_text (text, vowel_list):
#     phrase = list(map(lambda a: list(a), text.split(" ")))
#     vowel_quantity = []
#     for i in phrase:
#         count = 0
#         if set(i).intersection(set(vowel_list)):
#             for j in set(i).intersection(set(vowel_list)):
#                 count += i.count(j)
#         vowel_quantity.append(count)
#     return "Парам пам-пам" if len(set(vowel_quantity)) < 2 else "Пам парам"

def rhythm_text (text):
    phrase = list(map(lambda a: list(a), text.split(" ")))
    is_vowel = lambda word: word in {"а", "о", "у", "ы", "э", "я", "е", "ё", "ю", "и"}
    vowel_quantity = set(len(list(filter(is_vowel, i))) for i in phrase)
    return "Парам пам-пам" if len(vowel_quantity) < 2 else "Пам парам"

text = "пара-ра-рам рам-пам-папам па-ра-па-дам"
print(rhythm_text(text))