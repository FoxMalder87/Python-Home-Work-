number = int(input("Введите пятизначное число: "))
last = number % 10
number /= 10
new_number = last * 10000 + number
print(new_number)