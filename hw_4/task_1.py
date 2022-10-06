# задача 1. Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.

def find_size_list(us_num):
    fac = 2
    size = 0
    if us_num > 1:
        while us_num > 1:
            while us_num % fac != 0:
                fac += 1
            us_num = us_num / fac
            size += 1
    elif us_num == 1:
        size = us_num
    elif us_num == 0:
        size = us_num
    return size


def form_list_simple_factors(user_number, size):
    factor = 2
    simple_factors = []
    for i in range(size):
        if size == 1:
            list_fac = user_number
            simple_factors.append(list_fac)
            break
        while user_number % factor != 0:
            factor += 1
        user_number = user_number / factor
        list_fac = factor
        simple_factors.append(list_fac)
    return simple_factors

try:
    nat_num = int(input('Введите натуральное число: '))
    size_list = (find_size_list(nat_num))
    if size_list == 0:
        print(f'У {nat_num} нет множителей.')
    else:
        print(f'Множители числа {nat_num}: {form_list_simple_factors(nat_num, size_list)}')
except:
    print('Ошибка ввода данных!')