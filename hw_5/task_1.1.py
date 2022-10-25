# Игра с конфетами: человек против робота.

import random

def game_by_bot(am_can):
    while am_can > 84:
        candies = random.randint(1,28)
        break
    if am_can <= 84:
        if am_can <= 29:
            candies = am_can
        if am_can == 29:
            candies = random.randint(1,28)
        if am_can <= 56 and am_can > 29:
            per = 56 - am_can
            candies = 28 - per - 1
        if am_can <= 84 and am_can > 56:
            per = 84 - am_can
            candies = 28 - per - 2
    return candies
player = input('Введите имя игрока: ')
print(f'Игрок {player} играет против робота Аркадия.')

amount_candies = int(input('Введите количество конфет: '))

player_turn = random.randint(1,2)

player_candies_counter = 0
robot_candies_counter = 0

turn_counter = 37

while amount_candies > 0:
    if player_turn == 1:
        print(f'Ходит {player}.')
        chose_candies_player = int(input('Сколько конфет хотите взять? Можно взять не более чем 28 конфет. '))
        if chose_candies_player > 28 or chose_candies_player < 1:
            print('Неверное количество конфет. Можно взять от 1 до 28.')
        elif chose_candies_player > amount_candies:
            print(f'Сейчас можно взять не более чем {amount_candies} конфет')
        else:
            amount_candies -= chose_candies_player
            print(f'Осталось {amount_candies} конфет.')
            player_candies_counter += chose_candies_player
            print(f'Количество конфет у игрока {player} теперь {player_candies_counter}.')
            player_turn = 2
            last_turn = True
    else:
        print(f'Ходит робот Аркадий')
        chose_candies_robot = game_by_bot(amount_candies)
        if chose_candies_robot > 28 or chose_candies_robot < 1:
            print('Неверное количество конфет. Можно взять от 1 до 28.')
        elif chose_candies_robot > amount_candies:
            print(f'Сейчас можно взять не более чем {amount_candies} конфет')
        else:
            amount_candies -= chose_candies_robot
            print(f'Осталось {amount_candies} конфет.')
            robot_candies_counter += chose_candies_robot
            print(f'Количество конфет у робота Аркадия теперь {robot_candies_counter}.')
            player_turn = 1
            last_turn = False

if last_turn:
    print(f'Игрок {player} вправе забрать все конфеты робота Аркадия: {robot_candies_counter} конфет.')
    print(f'Теперь у игрока {player} {robot_candies_counter + player_candies_counter} конфет! {player} побеждает!')
else:
    print(f'Робот Аркадий вправе забрать все конфеты игрока {player}: {player_candies_counter} конфет.')
    print(f'Теперь у робота Аркадия {robot_candies_counter + player_candies_counter} конфет! Робот Аркадий побеждает!')