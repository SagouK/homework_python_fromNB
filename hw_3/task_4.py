# Задача 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

def decimal_to_binary(num):
    arr = []
    while num > 0:
        if num % 2 != 0:
            rest = 1
            arr.append(rest)
            num = num // 2
        else:
            rest = 0
            arr.append(rest)
            num = num // 2
    return arr

def sort_list(bin_num):
    for i in range(len(bin_num) // 2):
        box = bin_num[i]
        bin_num[i] = bin_num[len(bin_num) - i - 1]
        bin_num[len(bin_num) - i - 1] = box
    return bin_num

try:
    user_number = int(input('Введите любое целое число: '))
    unsort_binary_number = decimal_to_binary(user_number)
    print(f'Двоичное представление вашего числа = {sort_list(unsort_binary_number)}')
except:
    print('Ошибка ввода данных!')