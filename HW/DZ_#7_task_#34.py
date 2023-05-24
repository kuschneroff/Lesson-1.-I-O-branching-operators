'''''
Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает,
Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов
(т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры.
В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

*Пример:*

**Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
    **Вывод:** Парам пам-пам 
'''''


def check_rhythm(poem):
    phrases = poem.split()
    syllable_counts = list(map(count_syllables, phrases))
    if all(x == syllable_counts[0] for x in syllable_counts):
        return "Парам пам-пам"
    else:
        return "Пам парам"


def count_syllables(phrase):
    words = phrase.split('-')
    syllable_counts = list(map(count_vowels, words))
    total_syllables = sum(syllable_counts)
    return total_syllables


def count_vowels(word):
    vowels = "аеёиоуыэюя"
    vowel_count = len(list(filter(lambda x: x in vowels, word)))
    return vowel_count


poem = input("Введите стихотворение: ")

result = check_rhythm(poem)
print(result)
