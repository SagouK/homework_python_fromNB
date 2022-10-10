# задача 2. Задайте последовательность чисел. Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности.

import random

def create_set(size, min_value, max_value):
    arr = []
    for i in range(size):
        num = random.randint(min_value, max_value + 1)
        arr.append(num)
    return arr

def form_list_non_repeating(array):
    non_repeat = []
    for k in range(len(array)):
        num = array[k]
        non_repeat.append(num)
    for i in range(len(array)):
        for j in range(len(non_repeat)):
            if j in array:
                continue
            else:
                non_repeat.pop()
    return non_repeat
    

user_list = create_set(10, 1, 10)
print(user_list)
print(form_list_non_repeating(user_list))