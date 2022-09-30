# Задача 2. Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.

def calculate_numbers(user_number):
    counter = 1
    arr = []
    arr.append(counter)
    for i in range(2,user_number + 1):
        counter = counter * i
        arr.append(counter)
    return arr

try:
    num = int(input("Введите целое число: "))
    print(calculate_numbers(num))
except:
    print('Ошибка ввода данных!')