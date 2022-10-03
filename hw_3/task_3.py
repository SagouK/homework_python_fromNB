# Задача 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и 
# минимальным значением дробной части элементов.

import random

def create_list(size, min_value, max_value):
    arr = []
    for i in range(size):
        num = round(random.uniform(min_value, max_value), 3)
        arr.append(num)
    return arr

def find_min(original_list):
    min = original_list[0] % 1
    for i in range(len(original_list)):
        if (float(original_list[i]) % 1) < min:
            min = original_list[i] % 1
    print(f'Минимальное значение доброной части элемента = {round(min, 3)}')
    return min

def find_max(original_list):
    max = original_list[0] % 1
    for i in range(len(original_list)):
        if (float(original_list[i]) % 1) > max:
            max = original_list[i] % 1
    print(f'Максимальное значение доброной части элемента = {round(max, 3)}')
    return max

def find_diff_min_max(min_f, max_f):
    diff = round((max_f - min_f), 3)
    return diff

try:
    list_length = int(input('Введите размер списка: '))
    array = create_list(list_length, 1, 10)
    print(f'Наш массив: {array}')
    min_fractional = find_min(array)
    max_fractional = find_max(array)
    print(f'Разница между максимальным и минимальным значениями дробных частей элементов = {find_diff_min_max(min_fractional, max_fractional)}')
except:
    print('Ошибка ввода данных')