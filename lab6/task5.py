dog_age = int(input("Введите возраст собаки: "))
age1 = dog_age * 10.5
age2 = 2 * 10.5 + (dog_age - 2) * 4

if dog_age > 0:
    if dog_age in [1, 2]:
        print(f"Введенный вами год эквивалентен {age1} человеческим")
    elif dog_age >= 3:
        print(f"Введенный вам год эквивалентен {age2} человеческим")
elif dog_age == 0:
    print("Возвраст равен 0")
else:
    print("Он что, в утробе?")