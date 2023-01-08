import time
import json
import datetime
import logging

from aiogram import Bot, Dispatcher, executor, types


logging.basicConfig(level=logging.INFO)

API_TOKEN = "5727436665:AAErSdlUvrKFqQ6I7AwHy54F98uNkaaDFuE"

bot = Bot(token = API_TOKEN)
dp = Dispatcher(bot = bot)

employees = []

lastname = ''
firstname = '' 
birth_day = '' 
position = ''
time_work = '' 
home_place = ''
phone_number = ''
data_base = {'Фамилия': lastname, 'Имя': firstname, 'Дата рождения': birth_day, 'Должность': position, 'Стаж работы': time_work, 'Место жительства': home_place, 'Телефон': phone_number}

flag = 0

def save(employees):
    with open('base.json','w',encoding='utf-8') as bs:
        bs.write(json.dumps(employees,ensure_ascii=False))
    print('Наша БД успешно сохранена в файле base.json')

def load():
    try:
        global employees
        with open('base.json','r',encoding='utf-8') as bs:
            employees = json.load(bs)
        print('Наша БД успешно загружена')
    except:
        with open('base.json','w',encoding='utf-8') as bs:
            bs.write(json.dumps(employees,ensure_ascii=False))
    return employees


# def write_info_add_employee(data):
#     now = datetime.datetime.now()
#     with open('log.csv', 'a', encoding = 'utf-8') as file:
#         file.write('{}; {}\n'
#                     .format(now, data))

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    global employees
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name
    employees = load()
    logging.info(f'{user_id} {user_full_name}, {time.asctime()}')
    await message.reply(f'Привет {user_full_name}, база данных начинает работу! Введите команду /help, чтобы увидеть список всех комманд.')


@dp.message_handler(commands=['help'])
async def show_commands(message: types.Message):
    await message.reply('Добро пожаловать в базу данных сотрудников компании!\n\
    Меню:\n\
    1. /add_employee\n\
    2. /del_employee\n\
    3. /search_info_about_employee_by_filter\n\
    4. /show_all_employees')


@dp.message_handler(commands=['add_employee'])
async def add(message: types.Message):
    global flag
    flag = 1
    await echo(message)
    
@dp.message_handler(commands=['show_all_employees'])
async def show_all_employees(message: types.Message):
    employees = load()
    empls = ""
    for i in employees:
        print(f'{i["Фамилия"]} {i["Имя"]}\n')
        empls = empls + i["Фамилия"] + ' ' + i["Имя"] + '\n'
    await message.reply('Вот текущий список сотрудников.\n' + empls)

@dp.message_handler(commands=["del_employee"])
async def del_employee(message: types.Message):
    global flag
    flag = 'delemp'
    await echo(message)

@dp.message_handler(commands='search_info_about_employee_by_filter')
async def search_data_employee(message: types.Message):
    global flag
    flag = 'search'
    await echo(message)

@dp.message_handler(content_types=["text"])
async def echo(message: types.Message):
    global person_last
    global employees
    global flag
    global data_base
    employees = load()
    print("fl",flag)
    if flag == 1:
        await message.answer('Введите фамилию сотрудника.')
        flag = flag + 1
    elif flag == 2:
        lastname = message.text
        data_base['Фамилия'] = lastname
        await bot.send_message(message.chat.id,'Введите имя сотрудника. ')
        flag = flag + 1
    elif flag == 3:
        firstname = message.text
        data_base['Имя'] = firstname
        await bot.send_message(message.chat.id,'Введите дату рождения сотрудника. ')
        flag = flag + 1
    elif flag == 4:
        birth_day = message.text
        data_base['Дата рождения'] = birth_day
        flag = flag + 1
        await bot.send_message(message.chat.id,'Введите должность сотрудника. ')
    elif flag == 5:
        position = message.text
        data_base['Должность'] = position
        flag = flag + 1
        await bot.send_message(message.chat.id,'Введите стаж работы сотрудника. ')
    elif flag == 6:
        time_work = message.text
        data_base['Стаж работы'] = time_work
        flag = flag + 1
        await bot.send_message(message.chat.id,'Введите место жительства сотрудника. ')
    elif flag == 7:
        home_place = message.text
        data_base['Место жительства'] = home_place
        flag = flag + 1
        await bot.send_message(message.chat.id,'Введите телефон сотрудника. ')
    elif flag == 8:
        phone_number = message.text
        data_base['Телефон'] = phone_number
        flag = flag + 1
        await bot.send_message(message.chat.id,'Сотрудник успешно добавлен!')
        print(data_base)
        employees.append(data_base)
        save(employees)

    elif flag == 'delemp':
        await message.answer('Введите фамилию сотрудника, которого хотите удалить: ')
        flag = 'save'
    elif flag == 'save':
        delete_person = message.text
        save_emp = False
        for i in employees:
            if i["Фамилия"] == delete_person:
                print(employees)
                employees.remove(i)
                save(employees)
                save_emp = True
                await bot.send_message(message.chat.id, 'Сотрудник успешно удален!')
                break
        if save_emp == False:
            await bot.send_message(message.chat.id, 'Такого сотрудника нет в базе данных, либо вы ввели фамилию с маленькой буквы!')

    elif flag == 'search':
        await message.answer('Введите фамилию сотрудника, данные которого вы хотите найти.\n\
        Данные сотрудника:\n\
        1. Дата рождения.\n\
        2. Должность.\n\
        3. Стаж работы.\n\
        4. Место жительства.\n\
        5. Телефон.\n\
        6. Все данные.\n\
        7. Закрыть меню.')
        flag = 'emp'

    elif flag == 'emp':
        person_last = message.text
        flag = 'func'
        print(person_last)
        await message.answer('Введите цифру, соотвутствующую функции в меню')

    elif flag == 'func':
        data_search = message.text
        if data_search == '1':
            print(data_search)
            for i in employees:
                if person_last == i['Фамилия']:
                    await message.answer(i['Дата рождения'])
        elif data_search == '2':
            print(data_search)
            for i in employees:
                if person_last == i['Фамилия']:
                    await message.answer(i['Должность'])
        elif data_search == '3':
            print(data_search)
            print(person_last)
            for i in employees:
                if person_last == i['Фамилия']:
                    await message.answer(i['Стаж работы'])
        elif data_search == '4':
            print(data_search)
            for i in employees:
                if person_last == i['Фамилия']:
                    await message.answer(i['Место жительства'])
        elif data_search == '5':
            print(data_search)
            for i in employees:
                if person_last == i['Фамилия']:
                    await message.answer(i['Телефон'])
        elif data_search == '6':
            print(data_search)
            for i in employees:
                if person_last == i['Фамилия']:
                    await message.answer(i)
        elif data_search == '7':
            flag = 0
            await message.answer('Вы вышли из меню.')
         

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)