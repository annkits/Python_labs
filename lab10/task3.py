with open('file6.txt', 'r', encoding='utf8') as file6:
    content = file6.read()
    words = content.split()
    total_words = len(words)
    words_with_e = sum(1 for word in words if 'e' in word or 'E' in word)
    if total_words == 0:
        percentage = 0
    else:
        percentage = (words_with_e / total_words) * 100

    print(percentage)