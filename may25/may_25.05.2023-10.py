try:
    sales = float(input("Введите общую сумму продаж за месяц: "))
    summary = 250 + 0.1 * sales
except ValueError:
    print("Ошибка: Некорректный ввод данных. Введите число.")
else:
    print("Сумма с учетом комиссии:", summary)
finally:
    print("Завершение программы.")