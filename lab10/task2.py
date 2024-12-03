def find_word_in_file(word, filenames):
    for filename in filenames:
        with open(filename, 'r', encoding='utf8') as file:
            content = file.read()
            if word in content:
                print(f"Слово '{word}' найдено в файле {filename}")
            else:
                print(f"Слово '{word}' не найдено в файле {filename}")

word_to_find = "Academy"
file_names = ['file5.txt', 'file6.txt']

find_word_in_file(word_to_find, file_names)