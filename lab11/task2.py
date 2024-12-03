letter_scores = {
    '1': 'AEILNORSTU',
    '2': 'DG',
    '3': 'DCMP',
    '4': 'FHVWY',
    '5': 'K',
    '8': 'JX',
    '10': 'QZ'
}

def calculate_word_score(word):
    score = 0
    for letter in word.upper():
        for points, letters in letter_scores.items():
            if letter in letters:
                score += int(points)
                break
    return score

user_word = input("Введите слово: ")
score = calculate_word_score(user_word)
print(f"Количество очков за слово '{user_word}': {score}")