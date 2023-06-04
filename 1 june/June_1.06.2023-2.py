# Запрос слова у пользователя
word = input("Введите слово: ")

# Нахождение середины слова
middle = len(word) // 2

# Разбиение слова на две половины
first_half = word[:middle]
second_half = word[middle:]

# Вывод половин слова
print("Первая половина:", first_half)
print("Вторая половина:", second_half)