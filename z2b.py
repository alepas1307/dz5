# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# b) Подумайте как наделить бота ""интеллектом""

import random

def Smart_bot(sum,max):
    count=0
    while sum>0:
        if count==0:
            minus=sum%(max+1)
            if minus==0:
                minus=1
            count+=1
        else:
            minus=29-take
        return minus


name = input('Введи своё имя: ')

total_sweets = 2021
max = 28
min = 1
player1 = name
player2 = 'Бот'

num = random.randint(1,2)
print(f'Игрок {name} является Игроком {num}, т.е. ходит {num}-ым')
if num == 1: player = player1
else: player = player2

while True:
    if player == player1:
        take = int(input(f'{name},сколько конфет ты заберешь? '))
    else:
        take = Smart_bot(total_sweets,max)
        print(f'Бот: Я заберу {take}.')
    if take<min or take>max:
        print('Введено неверное число.')
    else:
        total_sweets = total_sweets-take
        print(f'Осталось конфет: {total_sweets}')
        if total_sweets == 0:
            print(f'Победил(а) {player}!')
            exit()
        if player == player1: player = player2
        else: player = player1