m = [
    [11, 12, 13, 14],
    [21, 22, 23, 24],
    [31, 32, 33, 34]
    ]

for i in range(len(m)):
    for j in range(len(m[i])):
        print(m[i][j], end = ' ')
    print()

print()
def transpose(m):
    rows = len(m) #кол-во строк
    cols = len(m[0]) #кол-во столбцов
    transposed = [[0] * rows for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = m[i][j]
    return transposed


result = transpose(m)

for i in range(len(result)):
    for j in range(len(result[i])):
        print(result[i][j], end = ' ')
    print()