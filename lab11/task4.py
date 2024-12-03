import PySimpleGUI as sg
from random import *

text_size = 12
sg.theme('LightPurple')

layout = [
    [sg.Text('Границы', font=('italic', text_size), justification='center', size=(40,1))],
    [sg.Image(filename='q.png', key='picture')],
    [sg.Text('Верхняя граница:', font=('italic', text_size), size=(20, 1)),
    sg.InputText(key = 'upper', font=('italic', text_size), size=(10, 1))],
    [sg.Text("Нижняя граница:", font=('italic', text_size), size=(20, 1)),
    sg.InputText(key = 'lower', font=('italic', text_size), size=(10, 1))],
    [sg.Button("Сгенерировать", font=('italic', text_size), size=(20, 1))],
    [sg.Text('', font=('italic', text_size), key='Output')],
]

window = sg.Window('Рандомайзер', layout)

while 1:
    event, values = window.read()
    if event == "Сгенерировать":
        low = int(values['lower'])
        up = int(values["upper"])
        if low > up:
            sg.popup_error("Некорректные границы", font=('italic', text_size))
        else:
            window["Output"].update(randint(low, up))
    elif event == sg.WINDOW_CLOSED:
        break

window.close()