import PySimpleGUI as sg
import random

c_image = [[sg.Image("bio.png")]]
c_input = [[sg.Text("Введите количество бактерий:", font="Arial 20"), sg.Input(font="Arial 20", size=(5, 0), key="micro")],
            [sg.Text("Введите коэффициент размножения:", font="Arial 20"), sg.Input(font="Arial 20", size=(5, 0), key="k")],
           [sg.Text("Количество секунд:", font="Arial 20"), sg.Input(font="Arial 20", size=(5, 0), key="count")],
           [sg.Text("Результат:", font="Arial 20"), sg.Input(font="Arial 20", readonly=True, size=(5, 0), key="res")],
           [sg.Button("Рассчитать", font="Arial 20")]]

layout = [
    [sg.Column(c_image), sg.VSeperator(), sg.Column(c_input, justification='right')]
]

window = sg.Window("Калькулятор бактерий", layout)

while 1:

    event, value = window.read()

    if event == sg.WIN_CLOSED:
        break

    micro = int(value["micro"])  #здесь хранится количество бактерий изначально
    count = int(value["count"])  #здесь хранится количество секунд для которых требуется рассчитать
    res = 0                 #здесь будет храниться результат
    b = random.randint(0, 4)
    k = int(value["k"])

    if event == "Рассчитать":
        for _ in range(count):
            res += k * micro + b
        window["res"].update(res)


window.close()

