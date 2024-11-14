sent = "Довольно распространённая ошибка ошибка это лишний повтор повтор слова слова Смешно не не правда ли Не нужно портить хор хоровод"

sent1 = sent.split()

for i in range(len(sent1) - 1):
    if sent1[i] != sent1 [i + 1]:
        print(sent1[i])

print(sent1[-1])
