word = input("Введите слово из пяти букв: ")

if len(word) != 5:
    print("Вы ввели слово неправильной длины.")
else:
    reversed_word = word[::-1]
    if word == reversed_word:
        print("Слово", word, "является палиндромом.")
    else:
        print("Слово", word, "не является палиндромом.")