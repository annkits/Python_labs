month = input("Введите название месяца: ")

if month in ['Январь', 'Март', 'Май', 'Июль', 'Август', 'Октябрь', 'Декабрь']:
    print("В этом месяце 31 день")
elif month in ['Апрель', 'Июнь', 'Сентябрь', 'Ноябрь']:
    print("В этом месяце 30 дней")
else:
    print("В этом месяце 28 дней, а в високосный год - 29")