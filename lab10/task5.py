def add_line_in_middle(filename, new_line):
    with open(filename, 'r+', encoding='utf8') as file:
        lines = file.readlines()
        total_lines = len(lines)
        middle_index = total_lines // 2
        lines.insert(middle_index, new_line + '\n')
        file.seek(0)
        file.writelines(lines)

filename = input("Введите имя файла: ")
new_line = input("Введите строку для добавления: ")

add_line_in_middle(filename, new_line)