def output_n_names(n, filename):
    with open(filename, 'r', encoding='utf8') as file:
        content = file.readlines()
        cnt = 0
        for name in content:
            print(name.split()[0])
            cnt += 1
            if n == cnt:
                break


n = int(input())
gender = input()

if gender == 'м':
    output_n_names(n, 'file8.txt')
else:
    output_n_names(n, 'file7.txt')