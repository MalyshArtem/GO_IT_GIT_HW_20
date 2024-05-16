# 1. Получаем гласные

# Этот пример возвращает в строке найденные гласные "a e i o u". Это может оказаться полезным при поиске или обнаружении гласных.

def get_vowels(String):
    return [each for each in String if each in "aeiou"]
get_vowels("animal") # [a, i, a]
get_vowels("sky") # []
get_vowels("football") # [o, o, a]
