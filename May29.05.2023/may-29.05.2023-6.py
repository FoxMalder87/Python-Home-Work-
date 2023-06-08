# VN: тут нужна обработка исключения
purchase_amount = float(input("Введите сумму покупки: "))

if 200 <= purchase_amount < 300:
    discount = 0.03
elif 300 <= purchase_amount < 500:
    discount = 0.05
elif purchase_amount >= 500:
    discount = 0.07
else:
    discount = 0

discounted_amount = purchase_amount - (purchase_amount * discount)
print("Сумма к оплате со скидкой:", discounted_amount)