# VN: тут нужна обработка исключения
usd_amount = float(input("Введите количество USD: "))
currency = input("Выберите валюту для конвертации (EUR, UAN, AZN): ")

if currency == "EUR":
    converted_amount = usd_amount * 0.8  
    print("Сумма в EUR:", converted_amount)
elif currency == "UAN":
    converted_amount = usd_amount * 27 
    print("Сумма в UAN:", converted_amount)
elif currency == "AZN":
    converted_amount = usd_amount * 1.7 
    print("Сумма в AZN:", converted_amount)
else:
    print("Выбрана недоступная валюта.")