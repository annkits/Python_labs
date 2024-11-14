menu = [
    ['Пицца Маргарита', ['мука', 'томаты', 'сыр', "базилик"], 10],
    ["Салат Цезарь", ["салат", "курица", "сыр", "сухарики"], 8],
    ["Суп Томатный", ["томаты", "лук", "морковь", "картофель"], 6]
    ]

def display_menu():
    for dish in menu:
        name = dish[0]
        ingredients = ', '.join(dish[1])
        price = dish[2]
        print(f"{name}:\n Ингредиенты: {ingredients}\n Цена: ${price}\n")

def find_dish(dish_name):
    for dish in menu:
        if dish_name.lower() == dish[0].lower():
            print(f"Найдено блюдо: \n {dish[0]}:\n  Ингредиенты: {', '.join(dish[1])}\n   Цена: ${dish[2]}\n")
            return
    print(f"Блюдо '{dish_name}' не найдено в меню.\n")

def new_dish(name, ingredients, price):
    menu.append([name, ingredients.split(','), int(price)])
    print(f"Блюдо '{name}' добавлено в меню.\n")
    display_menu()

def change_price(dish_name, new_price):
    for dish in menu:
        if dish_name.lower() == dish[0].lower():
            dish[2] = new_price
            print(f"Цена блюда '{dish[0]}' изменена на ${new_price}.\n")
            display_menu()
            return
    print(f"Блюдо '{dish_name}' не найдено в меню.\n")


choice = int(input("1. Отобразить меню ресторана.\n"
                   "2. Поиск блюда.\n"
                   "3. Добавить новое блюдо в меню.\n"
                   "4. Изменить цену блюда.\n"
                   "Ваш выбор: "))

if choice == 1:
    display_menu()
elif choice == 2:
    dish_name = input("Введите название блюда, которое вы ищете: ")
    find_dish(dish_name)
elif choice == 3:
    name = input("Введите название нового блюда: ")
    ingredients = input("Введите ингредиенты через запятую: ")
    price = int(input("Введите цену блюда: "))
    new_dish(name, ingredients, price)
elif choice == 4:
    dish_name = input("Введите название блюда, цену которого хотите изменить: ")
    try:
        new_price = int(input("Введите новую цену: "))
        change_price(dish_name, new_price)
    except ValueError:
        print("Ошибка: цена должна быть числом.\n")
else:
    print("Некорректный выбор. Попробуйте снова.")