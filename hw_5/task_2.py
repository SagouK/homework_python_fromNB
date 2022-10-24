# задача 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

def rle_alg(new_data):
    counter = 1
    dat_final = ''
    for i in range(len(new_data) - 1):
        if new_data[i] == new_data[i+1]:
            counter = counter + 1
        elif new_data[i] != new_data[i+1]:
            dat_final = dat_final + str(counter) + new_data[i]
            counter = 1
    return dat_final


data = open('data_rle.txt', 'r')
dat = data.read()
print(dat)

code_phrase = rle_alg(dat)
print(code_phrase)

data.close()

data1 = open('new_data_rle.txt', 'w')
data1.write(code_phrase)

data1.close()


    
