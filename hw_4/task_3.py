# задача 3. Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

import random

def find_nums(grade, min_value, max_value):
    polynomial = []
    for i in range(grade+1):
        part = random.randint(min_value, max_value + 1)
        polynomial.append(part)
    return polynomial

def form_polyl(arr, n):
    array = []
    for i in range(len(arr)):
        if n > 1:
            array.append(f'{arr[i]}x^{n} + ')
            n = n - 1
        elif n == 1:
            array.append(f'{arr[i]}x + ')
            n = n - 1
        elif n == 0:
            array.append(f'{arr[i]} = 0')
    
    return array

k = int(input('Введите степень многочлена: '))
poly = find_nums(k, 0, 100)
print(form_polyl(poly, k))
data = open('polynomial_k.txt', 'r')
data.close()


