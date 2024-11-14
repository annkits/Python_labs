bin_num = input("Введите двоичное число: ")
dec_num = 0
power = 0

for i in range(len(bin_num) - 1, -1, -1):
    if bin_num[i] == '1':
        dec_num = dec_num + 2 ** power
    power += 1

print(dec_num)