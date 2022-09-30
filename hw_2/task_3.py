# Задача 3. Реализуйте алгоритм перемешивания списка. 
# Список размерностью 10 задается случайными целыми числами, 
# выводится на экран, затем перемешивается, опять выводится на экран.

import random

def create_list(size, min_value, max_value):
    arr = []
    for i in range(size):
        num = random.randint(min_value, max_value)
        arr.append(num)
    return arr

def mix_list(array):
    for i in range(len(array) - 1):
        array[i], array[len(array) - 1] = array[len(array) - 1], array[i]
        array[i], array[len(array) // 2] = array[len(array) // 2], array[i]
        array[i], array[i+1] = array[i+1], array[i]
    return array

some_array = create_list(10, -10, 10)
print(some_array)
print(mix_list(some_array))