# Считывание данных с клавиатуры
movie = input("Введите название фильма: ")
theater = input("Введите название кинотеатра: ")
time = input("Введите время: ")

#вывод сообщения
message = "Билет на {} в {} на {} забронирован.".format(movie, theater, time)
print(message)

