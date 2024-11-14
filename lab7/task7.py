import random

length = int(input("Желаемая длина пароля (целое число): "))
upper = input("Нужны ли заглавные буквы (да/нет): ")
lower = input("Нужны ли строчные буквы (да/нет): ")
digit = input("Нужны ли цифры (да/нет): ")
special = input("Нужны ли специальные символы (да/нет): ")

alphabet_upper = "QWERTYUIOPASDFGHJKLZXCVBNM"
alphabet_lower = "qwertyuiopasdfghjklzxcvbnm"
alphabet_special = "@#$&*:;?><"

alphabet = ''
if upper == 'да':
    alphabet += alphabet_upper
if lower == 'да':
    alphabet += alphabet_lower
if digit == 'да':
    alphabet += str(random.randint(0,9))
if special == 'да':
    alphabet += alphabet_special

if not alphabet:
    print("Ошибка! Не выбран ни один тип символов для генерации пароля")
else:
    password = ''.join(random.choice(alphabet) for _ in range(length))
    print(f"Сгенерированный пароль: {password}")