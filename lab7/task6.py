word = input("Введите зашифрованное слово: ")

new1_word = ''

new2_word: str = ''

if word[-1] == '#':
    word = word[:-1]
    for i in range(len(word)):
        if i % 2 == 0:
            new1_word += word[i]
        else:
            new2_word = word[i] + new2_word
else:
    print("Ошибка! Отсутствует символ #")

print(new1_word+new2_word)