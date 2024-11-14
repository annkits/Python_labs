import random

a = []
cnt = 0
win = 0

while win != 1:
    cnt += 1
    O_R = random.choice(["О", "Р"])
    a.append(O_R)

    if len(a) >= 3 and a[-1] == a[-2] == a[-3]:
        win = 1
        print(a, f"(попыток: {cnt})")