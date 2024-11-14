height = list(map(int, input("Введите рост: ").split()))
Andrey_height = int(input("Рост Андрея: "))
formation = []

for i in range(len(height)):
    if Andrey_height <= height[i]:
        formation.append(i+2)

print(max(formation))