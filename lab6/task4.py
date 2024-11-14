n = int(input("Введите число: "))
b = -1

for i in range(n, 0, -1):
    b += 2
    print(" " * i, "#" * b)

print(" " * n, "#")