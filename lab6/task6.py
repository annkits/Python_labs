import random

print("Хорошо, я загадал число. Попробуй его отгадать")

def end():
    while True:
        answer = input("Хотите продолжить игру?")
        if answer == "Да":
            f()
        elif answer == "Нет":
            print("Хорошего времени суток :)")
            break
        elif answer != "Нет" and answer != "Да":
            print("Не понимаю :(")
            end()
def f():
    secret = random.randint(1, 10)
    cnt = 0
    while True:
        cnt += 1
        num = int(input("> "))
        if num < secret:
            print("Посдказка: загаданное число больше")
        elif num > secret:
            print("Подсказка: загаданное число меньше")
        elif num == secret:
            print("Поздравляю! Вы угадали!")
            end()
        else:
            print("Нее, ты не угадал. Попробуй снова")
f()