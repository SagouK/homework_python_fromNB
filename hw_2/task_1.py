# Задача 1. Напишите программу, которая принимает на вход вещественное или целое число 
# и показывает сумму его цифр. Через строку нельзя решать.

def sum_numbers(user_number):
    fraction_part = user_number
    whole_part = user_number
    sum = 0
    while user_number % 10 != 0:
        user_number = user_number * 10
    while user_number // 10 != 0:
        fraction_part = user_number % 10
        whole_part = user_number // 10
        user_number = whole_part
        sum = sum + fraction_part
           
    sum = sum + user_number
    return sum

num = float(input("Введите любое число: "))
print(f'Сумма цифр в вашем числе = {sum_numbers(num)}')
