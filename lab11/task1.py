keyboard_symbols = {
    '1': '.,?!:',
    '2': 'ABC',
    '3': 'DEF',
    '4': 'GHI',
    '5': 'JKL',
    '6': 'MNO',
    '7': 'PQRS',
    '8': 'TUV',
    '9': 'WXYZ',
    '0': ' '
}

def text_to_keypresses(text):
    result = []
    for char in text.upper():
        for key, chars in keyboard_symbols.items():
            if char in chars:
                result.append(key * (chars.index(char) + 1))
                break
    return ''.join(result)

user_input = input("Введите текст: ")
output = text_to_keypresses(user_input)
print(f"Последовательность кнопок: {output}")
