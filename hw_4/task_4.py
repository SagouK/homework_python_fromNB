# задача 4. Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) 
# этих двух чисел.

def find_simple_factors_num(m, n):
    if m > n:
        num_min = m
    else: 
        num_min = n
    while(True):
        if ((num_min % m == 0) and (num_min % n == 0)):
            lcm = num_min
            break
        num_min += 1
    return lcm
try:
    num_1 = int(input("Введите первое число: "))
    num_2 = int(input("Введите второе число: "))
    fac1 = find_simple_factors_num(num_1, num_2)
    print(fac1)
except:
    print('Ошибка ввода данных!')