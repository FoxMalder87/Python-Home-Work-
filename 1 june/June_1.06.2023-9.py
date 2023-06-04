def alternating_string(C1, C2, N):
    result = ""
    for i in range(N):
        if i % 2 == 0:
            result += C1
        else:
            result += C2
    return result

C1 = input("Введите символ C1: ")
C2 = input("Введите символ C2: ")
N = int(input("Введите длину строки: "))

output_string = alternating_string(C1, C2, N)
print("Результат: " + output_string)