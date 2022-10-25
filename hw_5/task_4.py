# задача 4. Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

import re

def data_to_list(plnml):
    arr = []
    for i in plnml:
        arr.append(i)
    return arr

def find_max_stp(data_list):
    for i in range(len(data_list)):
        if data_list[i] == '^':
            max_stp = data_list[i+1]
            break
    return max_stp

def del_stp(expression, grade):
    sp = []
    sp2 = []
    slov = {}
    for i in range(len(expression)):
        if expression[i] != str(grade):
            if expression[i].isdigit():
                sp.append(expression[i])
                if expression[i+1].isdigit():
                    sp.append(expression)
        elif expression[i] == str(grade):
            sp2.append(grade)
            grade = grade - 1
        elif expression[i] == 'x' and expression[i+1] != '^':
            sp2.append(1)
    print(sp, sp2)


data_1 = open('first_polynomial.txt', 'r')
data_2 = open('sec_polynomial.txt', 'r')
x1 = data_1.read()
x2 = data_2.read()
print(f'{x1}\n{x2}')
#new_list1 = data_to_list(x1)
#new_list2 = data_to_list(x2)

#print(new_list1, new_list2)

stp1 = int(find_max_stp(x1))
stp2 = int(find_max_stp(x2))

print(stp1, stp2)

exp_without_stp = del_stp(x1, stp1)

'''
for i in range(grade):
            if expression[i] != '*' or '+' or 'x' or '-' or ' ' or '^':
                print(expression[i]) '''