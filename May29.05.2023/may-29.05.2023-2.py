number = input("Введите трехзначное число: ")

if len(number) != 3 or not number.isdigit():
    print("Вы ввели некорректное трехзначное число.")
else:
    if number[0] == number[1] or number[1] == number[2] or number[0] == number[2]:
        print("В числе есть одинаковые цифры.")
    else:
        print("В числе нет одинаковых цифр.")