cnt = int(input("Сколько слов будет сокращено? "))
words = []

while cnt > 0:
    word = input()
    if len(word) <= 10:
        words.append(word)
    else:
        words.append(word[0] + str(len(word) - 2) + word[-1])
    cnt -= 1

for word in words:
    print(word)