try:
    Enter_a_three_digit_number = int(input("Введите трехзначное число: "))
    if Enter_a_three_digit_number < 100 or Enter_a_three_digit_number > 999:
    # VN: Здорово, что вы разобрались с raise. В будущем его так не используйте.
    # т.е. число не находится в диапазоне - это не исключительная ситуация
        raise ValueError("Ошибка: Введено число, не являющееся трехзначным.")
    division = (Enter_a_three_digit_number / 10) % 10
except ValueError as e:
    print(str(e))
else:
    print("Результат:", division)
finally:
    print("Завершение программы.")