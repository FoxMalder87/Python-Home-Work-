# Запрос слова у пользователя
word = input("Введите слово: ")

# Зацензурирование слова
censored_word = word[0] + "*" * (len(word) - 2) + word[-1]

# Вывод зацензурированного слова
print("Зацензурированное слово:", censored_word)