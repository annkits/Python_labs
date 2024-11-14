n = int(input("Введите количество строк n: "))
m = int(input("Введите количество столбцов m: "))

matrix = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if i == 0 or j == 0:
            matrix[i][j] = 1 #Первые строка и столбец равны 1
        else:
            matrix[i][j] = matrix[i-1][j] + matrix[i][j-1] #Сумма сверху и слева

print("\nСформированная матрица: ")
for row in matrix:
    for elem in row:
        print(f"{elem:6}", end="") #Каждый элемент занимает ровно 6 символов
    print()