def f(x):
    return x**2 / (10 + x**3)

a = int(input("Введите значение a: "))
b = int(input("Введите значение b: "))
n = int(input("Введите количество разбиений n: "))
def trap(a, b, n):
    h = (b - a)/n
    integral = (f(a) + f(b))/2 #Начальное значение - сумма значений на границах
    for i in range (1, n): #Проходим по внутренним точкам (без границ)
        integral += f(a+i*h)
    return integral*h #Умножаем итоговую сумму на шаг h

print(trap(a, b, n))
