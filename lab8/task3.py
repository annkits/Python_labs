numbers = input("Введите список: ")

numbers = [int(num) for num in numbers.split()]

result_list = [numbers[i] for i in range(1, len(numbers)) if numbers[i] > numbers[i-1]]

print(result_list)