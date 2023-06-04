try:
    # VN: input не нужно помещать в try! Вычисления - тоже, кроме деления. Это касается всех задач
    user_input = input("Введите число: ")
    user_int = int(user_input)
except ValueError:
    print("Ошибка: Некорректный ввод данных. Введите целое число.")
else:
    result = user_int ** 2
    print("Результат:", result)
finally:
    print("Завершение программы.")