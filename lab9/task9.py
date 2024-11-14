import random

size = 4

field = [['.'] * size for _ in range(size)]
hidden_field = [['.'] * size for _ in range(size)]

ships = set()
while len(ships) < 4:
    x, y = random.randint(0, size - 1), random.randint(0, size - 1)
    ships.add((x, y))
    hidden_field[x][y] = 'S'

while True:
    bomb_x, bomb_y = random.randint(0, size - 1), random.randint(0, size - 1)
    if (bomb_x, bomb_y) not in ships:
        hidden_field[bomb_x][bomb_y] = 'B'
        break

print("Добро пожаловать в игру 'Морской бой'!")
print("На поле 4 корабля и 1 бомба. Найдите все корабли, чтобы победить.")
print("При попадании в бомбу — игра окончена.")
print("Формат ввода: две координаты (строка и столбец) через пробел.")

hits = 0
steps = 0
game_over = False

while not game_over:
    print("\nТекущее поле:")
    for row in field:
        print(" ".join(row))

    try:
        x, y = map(int, input("Введите координаты выстрела (строка столбец): ").split())
        if not (1 <= x <= size and 1 <= y <= size):
            print("Координаты вне диапазона. Попробуйте снова.")
            continue
        x -= 1
        y -= 1
    except ValueError:
        print("Некорректный ввод. Попробуйте снова.")
        continue
    steps += 1

    if hidden_field[x][y] == 'S':
        print("Попадание!")
        field[x][y] = 'X'
        hidden_field[x][y] = '.'
        hits += 1
        if hits == 4:
            print("\nПоздравляем! Вы нашли все корабли!")
            print(f"Вы победили за {steps} шагов.")
            game_over = True
    elif hidden_field[x][y] == 'B':
        print("Вы попали на бомбу! Игра окончена.")
        field[x][y] = 'B'
        game_over = True
    else:
        print("Мимо!")
        field[x][y] = '*'

print("\nФинальное поле:")
for row in field:
    print(" ".join(row))