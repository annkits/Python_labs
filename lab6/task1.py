heights = []

height = int(input("Введите рост: "))

while height != 0:
    if height > 0:
        heights.append(height)
    height = int(input("Введите рост: "))

if len(heights) < 2:
    print("Некого сравнивать")
else:
    print(f"Самый высокий человек с ростом: {max(heights)}")
    print(f"Самый низкий человек с ростом: {min(heights)}")
