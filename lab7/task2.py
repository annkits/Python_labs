a = input("Введите два слова: ")

a = a.split(' ')

if len(a) == 2:
    a = a[::-1]
    print(' '.join(a))
else:
    print("Ошибка! Некорректное количество слов")

