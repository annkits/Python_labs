rooms = int(input("Сколько комнат в общежитии? "))

cnt = 0

while rooms != 0:
    free_space = input().split()
    if free_space[0] < free_space[1]:
        cnt += 1
    rooms -= 1

print(cnt)