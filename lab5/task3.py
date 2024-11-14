number = int(input("Введите трёхзначное число: "))

output_number = sum(int(digit) for digit in str(number))

print(f"Сумма цифр числа: {output_number}")