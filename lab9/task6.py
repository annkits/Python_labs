matrix = []

n = int(input("Введите количество строк и столбцов: "))

print("Заполните матрицу (вводите по одному элементу): ")
for i in range(n):
    line = []
    for j in range(n):
        line.append(input())
    matrix.append(line)

print("Исходная матрица:")
for i in range(n):
    for j in range(n):
        print(matrix[i][j], end = " ")
    print()

for i in range(n):
    j = n - 1 - i #индекс элемента на побочной диагонали в текущем столбце
    matrix[i][i], matrix[j][i] = matrix[j][i], matrix[i][i]

print("\nМатрица после перестановки диагоналей: ")
for i in range(n):
    for j in range(n):
        print(matrix[i][j], end = " ")
    print()