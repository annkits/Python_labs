n = int(input("Введите число: "))
i = 1
a = 0

while i < n + 1:
    a += i ** 2
    i += 1

print(a)