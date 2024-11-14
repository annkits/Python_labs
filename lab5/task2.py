number = int(input("Введите число: "))
k = int(input("Введите количество исключаемых цифр: "))

output_number = number % (10 ** k)

print(f"Получившееся число: {output_number}")