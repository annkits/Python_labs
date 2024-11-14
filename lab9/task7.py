matrix = []

n = int(input("Введите количество рядов: "))
m = int(input("Введите количество мест: "))

print("Заполните места (вводите по одному элементу): ")
for i in range(n):
    line = []
    for j in range(m):
        line.append(input())
    matrix.append(line)

print("\nСхема мест:")
for i in range(n):
    for j in range(m):
        print(matrix[i][j], end=" ")
    print()

k = int(input("\nВведите количество билетов в заказе: "))

found = False
for i in range(n):
    row = ''.join(matrix[i]) #Преобразуем ряд в строку
    if '0'*k in row:
        print(f"Ряд {i+1} подходит для бронирования.")
        found = True
        break

if not found:
    print("Мест нет.")