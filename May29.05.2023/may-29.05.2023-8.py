score = 0

print("Вопрос 1: Каким из цветов бывает собака породы лабродор?")
print("a) Коричневый")
print("b) фиолетовый")
print("c) Красный")

answer1 = input("Ваш ответ: ")
if answer1.lower() == "a":
    score += 2

print("Вопрос 2: Столица Казахстана?")
print("a) Париж")
print("b) Атырау")
print("c) Астана")

answer2 = input("Ваш ответ: ")
if answer2.lower() == "c":
    score += 2

print("Вопрос 3: Кто написал произведение 'Война и мир'?")
print("a) Достоевский")
print("b) Толстой")
print("c) Тургенев")

answer3 = input("Ваш ответ: ")
if answer3.lower() == "b":
    score += 2

print("Вы набрали", score, "баллов.")