# Задача 1. Создайте программу для игры в "Крестики-нолики".

import random


def print_field(size, field):
    for i in range(size):
        print(' '.join(field[i]))

def take_turn(field, turn, hor, vert):
    for i in range(len(field)):
        for j in range(len(field)):
            if i == hor and j == vert:
                field[i][j] = turn
    return field

def check_winner(our_field, isturn):
    if our_field[0][0] == our_field[0][1] == our_field[0][2] == isturn or \
        our_field[1][0] == our_field[1][1] == our_field[1][2] == isturn or \
        our_field[2][0] == our_field[2][1] == our_field[2][2] == isturn or \
        our_field[0][0] == our_field[1][0] == our_field[2][0] == isturn or \
        our_field[0][1] == our_field[1][1] == our_field[2][1] == isturn or \
        our_field[0][2] == our_field[1][2] == our_field[2][2] == isturn or \
        our_field[0][0] == our_field[1][1] == our_field[2][2] == isturn or \
        our_field[0][2] == our_field[1][1] == our_field[2][0] == isturn:
        return isturn
    else:
        return False


player_1 = input('Введите имя первого игрока: ')
player_2 = input('Введите имя второго игрока: ')

size_field = int(input('Введите размер игрового поля: '))

dot_none = '.'
columns = []

for i in range(size_field):
    rows = []
    for j in range(size_field):
        rows.append(dot_none)
    columns.append(rows)


print_field(size_field, columns)      
player_turn = random.randint(1,2)


turn_x = 'x'
turn_o = '0'

if player_turn == 1:
    turn_1 = turn_x
    turn_2 = turn_o
else:
    turn_2 = turn_x
    turn_1 = turn_o

changed_field = columns


counter_turns = 0


while counter_turns <= 9:
    
    if player_turn == 1:
        print(f'Ходит игрок {player_1}')
        spot_horizontal = int(input('Выберите номер ячейки по горизонтали: '))
        spot_vertical = int(input('Выберите номер ячейки по вертикали: '))
        if changed_field[spot_horizontal][spot_vertical] == turn_x or changed_field[spot_horizontal][spot_vertical] == turn_o: 
            print('Место уже занято! Выберите другую ячейку.')
        else:
            changed_field = take_turn(columns, turn_1, spot_horizontal, spot_vertical)
            lol = check_winner(changed_field, turn_1)
            if lol:
                print(f'Выйграл игрок {player_1}!')
                print_field(size_field, changed_field)
                break
            else:
                print_field(size_field, changed_field)
                player_turn = 2
                counter_turns += 1
                if counter_turns == 9:
                    break
    else:
        print(f'Ходит игрок {player_2}')
        spot_horizontal = int(input('Выберите номер ячейки по горизонтали: '))
        spot_vertical = int(input('Выберите номер ячейки по вертикали: '))
        if changed_field[spot_horizontal][spot_vertical] == turn_x or changed_field[spot_horizontal][spot_vertical] == turn_o:
            print('Место уже занято! Выберите другую ячейку.')
        else:
            changed_field = take_turn(columns, turn_2, spot_horizontal, spot_vertical)
            lol = check_winner(changed_field, turn_2)
            if lol:
                print(f'Выйграл игрок {player_2}!')
                print_field(size_field, changed_field)
                break
            else:
                print_field(size_field, changed_field)
                player_turn = 1
                counter_turns += 1
                if counter_turns == 9:
                    break
if counter_turns == 9:
    print('Ничья!')    


