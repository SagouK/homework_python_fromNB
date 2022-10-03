# Задача 2. Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

def create_list(size):
    arr = []
    for i in range(size):
        try:
            num = int(input("Введите любое целое число: "))
        except:
            print('Ошибка ввода данных!')
        arr.append(num)
    return arr

def prod_couple(original_list):
    prod = 0
    sec_array = []
    if len(original_list) % 2 != 0:
        length = int(len(original_list) // 1.5)
        for i in range(length):
            prod = original_list[i] * original_list[(len(original_list) - i - 1)]
            sec_array.append(prod)
    elif len(original_list) % 2 == 0:
        for i in range(len(original_list) // 2):
            prod = original_list[i] * original_list[(len(original_list) - i - 1)]
            sec_array.append(prod)
    return sec_array

try:
    list_length = int(input('Введите размер списка: '))
    array = create_list(list_length)
    print(f'Наш массив: {array}')
    print(f'Произведение пар элементов = {prod_couple(array)}')
except:
    print('Ошибка ввода данных')