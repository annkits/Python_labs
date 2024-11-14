list = input("Введите список данных: ")

letters = [i for i in list if i.isalpha()]
numbers = [i for i in list if i.isdigit()]

del list

print(f"Список букв: {letters}")
print(f"Список цифр: {numbers}")
