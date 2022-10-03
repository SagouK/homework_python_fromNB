# Задача 1 Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.

def create_list(size):
    arr = []
    for i in range(size):
        try:
            num = int(input("Введите любое целое число: "))
        except:
            print('Ошибка ввода данных!')
        arr.append(num)
    return arr

def find_sum_odd(original_list):
    sum = 0
    for i in range(len(original_list)):
        if i % 2 != 0:
            sum += original_list[i]
    return sum

try:
    list_length = int(input('Введите размер списка: '))
    array = create_list(list_length)
    print(f'Сумма элементов, стоящих на нечетных позициях = {find_sum_odd(array)}')
except:
    print('Ошибка ввода данных!')
