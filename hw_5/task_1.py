'''задача 1. Создайте программу для игры с конфетами человек против человека.
Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
чтобы забрать все конфеты у своего конкурента?'''

import random


player_1 = input('Введите имя первого игрока: ')
player_2 = input('Введите имя второго игрока: ')

amount_candies = int(input('Введите количество конфет: '))

player_turn = random.randint(1,2)


player_1_candies_counter = 0
player_2_candies_counter = 0

while amount_candies > 0:
    if player_turn == 1:
        print(f'Ходит {player_1}.')
        chose_candies_1 = int(input('Сколько конфет хотите взять? Можно взять не более чем 28 конфет. '))
        if chose_candies_1 > 28 or chose_candies_1 < 1:
            print('Неверное количество конфет. Можно взять от 1 до 28.')
        elif chose_candies_1 > amount_candies:
            print(f'Сейчас можно взять не более чем {amount_candies} конфет')
        else:
            amount_candies -= chose_candies_1
            print(f'Осталось {amount_candies} конфет.')
            player_1_candies_counter += chose_candies_1
            print(f'Количество конфет у игрока {player_1} теперь {player_1_candies_counter}.')
            player_turn = 2
            last_turn = True
    else:
        print(f'Ходит {player_2}')
        chose_candies_2 = int(input('Сколько конфет хотите взять? Можно взять не более чем 28 конфет. '))
        if chose_candies_2 > 28 or chose_candies_2 < 1:
            print('Неверное количество конфет. Можно взять от 1 до 28.')
        elif chose_candies_2 > amount_candies:
            print(f'Сейчас можно взять не более чем {amount_candies} конфет')
        else:
            amount_candies -= chose_candies_2
            print(f'Осталось {amount_candies} конфет.')
            player_2_candies_counter += chose_candies_2
            print(f'Количество конфет у игрока {player_2} теперь {player_2_candies_counter}.')
            player_turn = 1
            last_turn = False

if last_turn:
    print(f'Игрок {player_1} вправе забрать все конфеты игрока {player_2}: {player_2_candies_counter} конфет.')
    print(f'Теперь у игрока {player_1} {player_1_candies_counter + player_2_candies_counter} конфет! {player_1} побеждает!')
else:
    print(f'Игрок {player_2} вправе забрать все конфеты игрока {player_1}: {player_1_candies_counter} конфет.')
    print(f'Теперь у игрока {player_2} {player_1_candies_counter + player_2_candies_counter} конфет! {player_2} побеждает!')

