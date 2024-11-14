a = input("Введите стих: ")

def f(a):
    gl = 'уеыаоэюияёУЕЫАОЭЮИЯЁ'
    cnt = 0
    for i in range(len(a)):
        if a[i] in gl:
            cnt += 1
    return cnt

b = a.split('/')

if len(b) == 3:
    a1, a2, a3 = b[0], b[1], b[2]
    if f(a1) == 5 and f(a2) == 7 and f(a3) == 5:
        print("Хайку!")
    else:
        print("Не хайку.")
else:
    print("Не хайку. Должно быть 3 строки.")