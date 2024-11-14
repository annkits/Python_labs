card_number = input("Введите номер карты: ")
sum_even = 0
sum_odd = 0

for i in range(len(card_number)): #
    digit = int(card_number[i]) #Преобразуем символ в число
    if i % 2 != 0: #Если индекс нечетный
        sum_even += digit
    else: #Для четных индексов
        doubled = digit * 2
        if doubled <= 9:
            sum_odd += doubled
        else:
            sum_odd += (doubled - 9)

if (sum_odd + sum_even) % 10 == 0:
    print("Корректный номер")
else:
    print("Некорректный номер")