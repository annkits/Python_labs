import PySimpleGUI as sg


def to_binary(number, bits=8):
    if number >= 0:
        return f"{number:0{bits}b}"
    else:
        return f"{(1 << bits) + number:0{bits}b}"


def calculate_codes(number):
    if not -128 <= number <= 127:
        raise ValueError("Число должно быть в диапазоне от -128 до 127.")
    bits = 8
    sign_bit = '0' if number >= 0 else '1'

    #Прямой код
    abs_binary = to_binary(abs(number), bits - 1)
    direct_code = sign_bit + abs_binary

    #Обратный код
    if number >= 0:
        reverse_code = direct_code
    else:
        inverted = ''.join('1' if bit == '0' else '0' for bit in abs_binary)
        reverse_code = sign_bit + inverted

    #Дополнительный код
    if number >= 0:
        additional_code = direct_code
    else:
        additional_code = to_binary((1 << bits)+number, bits)

    return direct_code, reverse_code, additional_code

layout = [
    [sg.Text("Введите число (-128 до 127):", font="Arial 16"), sg.Input(key="input_num", font="Arial 16", size=(10, 1))],
    [sg.Text("Прямой код:", font="Arial 16"), sg.Input(readonly=True, key="direct_code", font="Arial 16", size=(20, 1))],
    [sg.Text("Обратный код:", font="Arial 16"), sg.Input(readonly=True, key="reverse_code", font="Arial 16", size=(20, 1))],
    [sg.Text("Дополнительный код:", font="Arial 16"), sg.Input(readonly=True, key="additional_code", font="Arial 16", size=(20, 1))],
    [sg.Button("Рассчитать", font="Arial 16")]
]

window = sg.Window("Коды числа", layout)

while 1:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == "Рассчитать":
        number = int(values['input_num'])
        direct, reverse, additional = calculate_codes(number)
        window['direct_code'].update(direct)
        window['reverse_code'].update(reverse)
        window['additional_code'].update(additional)

window.close()