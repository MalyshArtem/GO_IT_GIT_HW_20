# 1. Получаем гласные

# Этот пример возвращает в строке найденные гласные "a e i o u". Это может оказаться полезным при поиске или обнаружении гласных.

def get_vowels(String):
    return [each for each in String if each in "aeiou"]
get_vowels("animal") # [a, i, a]
get_vowels("sky") # []
get_vowels("football") # [o, o, a]

# 2. Первая буква в верхнем регистре

# Этот пример используется для превращения каждой первой буквы символов строки в прописную букву. Он работает со строкой из одного или нескольких символов и будет полезен при анализе текста или записи данных в файл и т.п.

def capitalize(String):
    return String.title()
capitalize("shop") # [Shop]
capitalize("python programming") # [Python Programming]
capitalize("how are you!") # [How Are You!]