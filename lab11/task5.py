import PySimpleGUI as sg

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

# user_word = input("Введите слово: ")
# score = calculate_word_score(user_word)
# print(f"Количество очков за слово '{user_word}': {score}")

text_size = 12
sg.theme('TanBlue')

layout = [
    [sg.Text('Эрудит', font=('roman', text_size), justification='center', size=(40,1))],
    [sg.Text('Ваше слово: ', font=('roman', text_size), size=(20, 1)),
    sg.InputText(key='user_word', font=('roman', text_size), size=(20, 1))],
    [sg.Button("Узнать количество баллов", font=('roman', text_size), size=(40, 1))],
    [sg.Text('', font=('roman', text_size), key='Output')],
]

window = sg.Window('Эрудит', layout)

while 1:
    event, values = window.read()
    if event == "Узнать количество баллов":
        score = calculate_word_score(values['user_word'])
        window['Output'].update(score)
    elif event == sg.WINDOW_CLOSED:
        break

window.close()