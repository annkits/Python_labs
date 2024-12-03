import random


def generate_password(filename):
    with open(filename, 'r', encoding='utf8') as file:
        words = [word.strip() for word in file.readlines()]
        valid_words = [word for word in words if len(word) >= 3]

        while True:
            word1, word2 = random.sample(valid_words, 2)
            password = word1.capitalize() + word2.capitalize()
            if 8 <= len(password) <= 10:
                print(f"Сгенерированный пароль: {password}")
                break


filename = input("Введите имя файла со списком слов: ")
generate_password(filename)