def decrypt_file(filename):
    with open(filename, 'r', encoding='utf8') as file:
        lines = file.readlines()
        decrypted_lines = []
        for line in lines:
            decrypted_line = ' '.join(word[::-1] for word in line.split())
            decrypted_lines.append(decrypted_line)
        print("Расшифрованное сообщение:")
        print('\n'.join(decrypted_lines))


filename = input("Введите имя файла для дешифрования: ")
decrypt_file(filename)


def encrypt_file(input_filename, output_filename):
    with open(input_filename, 'r', encoding='utf8') as input_file:
        lines = input_file.readlines()
        encrypted_lines = []
        for line in lines:
            encrypted_line = ' '.join(word[::-1] for word in line.split())
            encrypted_lines.append(encrypted_line)
    with open(output_filename, 'w', encoding='utf8') as output_file:
        output_file.write('\n'.join(encrypted_lines))


input_filename = input("Введите имя исходного файла для шифрования: ")
output_filename = input("Введите имя файла для сохранения шифрованного текста: ")
encrypt_file(input_filename, output_filename)