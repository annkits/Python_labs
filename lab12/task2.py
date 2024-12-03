message_count = int(input("Количество сообщений: "))
dialog = input("Введите типы сообщений: ")


def valid_dialog(messages):
    qa = []
    for message in messages:
        if message == 'Q' or message == 'q':
            qa.append(message)
        elif message == 'A' or 'a':
            if not qa:
                return False
            qa.pop()
    return len(qa) == 0


if valid_dialog(dialog):
    print("+")
else:
    print("-")