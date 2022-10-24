# задача 3. Напишите программу, удаляющую из текста все слова, содержащие "абв".


def del_object(some_list):
    for i in some_list:
        if 'абв' in i:
            some_list.remove(i)
    return some_list

data = open('some text.txt', 'r', encoding = 'utf-8')
dat = data.read()
print(dat)

sp = dat.split()

final_text = del_object(sp)

new_string = ' '.join(final_text)
print(new_string)

data = open('some text.txt', 'a', encoding = 'utf-8')
data.write(new_string + '\n')

data.close()




