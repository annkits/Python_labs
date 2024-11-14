n = int(input("Введите количество сокровищ (n): "))
print("Введите координаты сокровищ (x y): ")

treasures = [list(map(int, input().split())) for _ in range(n)]

sasha = list(map(int, input("Введите координаты Александра (x y): ").split()))

def calculate_distance(point1, point2):
    return ((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)**0.5

min_distance = float('inf')
closest_treasure = None

for treasure in treasures:
    distance = calculate_distance(sasha, treasure)
    if distance < min_distance:
        min_distance = distance
        closest_treasure = treasure

print(f"Минимальное расстояние до сокровища: {min_distance}")
print(f"Координаты ближайшего сокровища: {closest_treasure}")