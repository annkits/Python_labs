numbers = input("Введите числа: ")

below = []
above = []
equal = []

digit = [int(num) for num in numbers.split()]

summary = sum(digit)
average = summary / len(digit)

for i in range(len(digit)):
    if digit[i] > average:
         above.append(digit[i])
    elif digit[i] < average:
        below.append(digit[i])
    else:
        equal.append(digit[i])

print(f'Среднее значение ряда: {average}')
print(f'Числа ниже среднего: {below}')
print(f'Числа, которые равны среднему: {equal}')
print(f'Числа выше среднего: {above}')