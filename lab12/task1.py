#Возвращает ключ сортировки для члена экипажа: приоритет эвакуации, индекс
def priority(member):
    priority_map = {
        'woman': 1,
        'child': 1,
        'man': 2,
        'captain': 3
    }
    return (priority_map[member[1]], member[2])


def evacuation_order():
    n = int(input("Введите количество членов экипажа: "))
    crew = []

    for i in range(n):
        name, status = input("Введите имя и статус через пробел: ").split()
        crew.append((name, status, i))

    # Метод .sort() с передачей функции priority для определения порядка сортировки
    crew.sort(key=priority)

    print("Порядок эвакуации: ")
    for person in crew:
        print(person[0])


evacuation_order()
