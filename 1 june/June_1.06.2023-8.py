purchase_price = float(input("Введите стоимость покупки в долларах ($): "))
discount_percentage = float(input("Введите размер скидки в процентах (%): "))

discount_amount = purchase_price * (discount_percentage / 100)
total_amount = purchase_price - discount_amount

print("Сумма покупки: $%.2f" % purchase_price)
print("Размер скидки: %.2f%%" % discount_percentage)
print("Сумма к оплате: $%.2f" % total_amount)