days = int(input("Введите количество дней: "))
hours = int(input("Введите количество часов: "))
minutes = int(input("Введите количество минут: "))
seconds = int(input("Введите количество секунд: "))

total_seconds = (days * 24 * 3600) + (hours * 3600) + (minutes * 60) + (seconds)

print(f"Общее количество секунд: {total_seconds}")
