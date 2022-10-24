# задача 4. Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.



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

def sum_polynomials(expression, grade):
    while grade < 0: print(grade)
        #if expression[i] != '*' or '+' or 'x' or '-' or ' ' or '^':
        #   array.append(expression[i])

data_1 = open('first_polynomial.txt', 'r')
data_2 = open('sec_polynomial.txt', 'r')
x1 = data_1.read()
x2 = data_2.read()

new_list1 = data_to_list(x1)
new_list2 = data_to_list(x2)

stp1 = int(find_max_stp(new_list1))
stp2 = find_max_stp(new_list2)

sum_polynomials(new_list1, stp1)

'''
for i in range(grade):
            if expression[i] != '*' or '+' or 'x' or '-' or ' ' or '^':
                print(expression[i]) '''