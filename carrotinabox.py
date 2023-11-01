"""Морковка в коробке, (C) Al Sweigart al@inventwithpython.com
Несерьезная игра с блефом для двух игроков-людей. В ее основе лежит
игра из телепрограммы, 8 Out of 10 Cats.
Код размещен на https://nostarch.com/big-book-small-python-programming
Теги: большая, для начинающих, игра, для двух игроков"""

import random

print('''Морковка в коробке, (C) Al Sweigart al@inventwithpython.com

Это игра в блеф для двух игроков-людей. У каждого игрока есть коробка.
В одной коробке лежит морковь. Чтобы выиграть, у вас должна быть коробка с
морковкой внутри.

Это очень простая и глупая игра.

Первый игрок заглядывает в свою коробку (при этом второй игрок должен закрыть
глаза). Затем первый игрок говорит: "В моем ящике есть морковка" или "В моем ящике нет морковки". 
Затем второй игрок должен решить, хочет ли он поменять коробки местами или нет.
''')
input('Нажмите Enter, чтобы начать...')

p1Name = input('Игрок-человек 1, введите свое имя: ')
p2Name = input('Игрок-человек 2, введите свое имя: ')
playerNames = p1Name[:11].center(11) + '    ' + p2Name[:11].center(11)

print('''ЕСТЬ ДВЕ КОРОБКИ:
  __________     __________
 /         /|   /         /|
+---------+ |  +---------+ |
|   RED   | |  |   GOLD  | |
|   BOX   | /  |   BOX   | /
+---------+/   +---------+/''')

print()
print(playerNames)
print()
print(p1Name + ', перед вами RED коробка.')
print(p2Name + ', перед вами GOLD коробка.')
print()
print(p1Name + ', вы сможете заглянуть в свою коробку.')
print(p2Name.upper() + ', закрой глаза и не подглядовай!!!')
input('Когда ' + p2Name + ' закроет глаза, нажмите Enter...')
print()

print(p1Name + ' вот внутренняя часть вашей коробки:')

if random.randint(1, 2) == 1:
    carrotInFirstBox = True
else:
    carrotInFirstBox = False

if carrotInFirstBox:
    print('''
   ___VV____
  |   VV    |
  |   VV    |
  |___||____|    __________
 /    ||   /|   /         /|
+---------+ |  +---------+ |
|   RED   | |  |   GOLD  | |
|   BOX   | /  |   BOX   | /
+---------+/   +---------+/
 (морковка!)''')
    print(playerNames)
else:
    print('''
   _________
  |         |
  |         |
  |_________|    __________
 /         /|   /         /|
+---------+ |  +---------+ |
|   RED   | |  |   GOLD  | |
|   BOX   | /  |   BOX   | /
+---------+/   +---------+/
(нет морковки!)''')
    print(playerNames)

input('Press Enter to continue...')

print('\n' * 100)  # Clear the screen by printing several newlines.
print(p1Name + ', скажите ' + p2Name + ' открыть глаза.')
input('Press Enter to continue...')

print()
print(p1Name + 'произнесите одно из следующих предложений, чтобы' + p2Name + '.')
print('  1) В моей коробке есть морковка.')
print('  2) В моей коробке нет ни одной морковки.')
print()
input('Then press Enter to continue...')

print()
print(p2Name + ', вы хотите поменять местами коробки с ' + p1Name + '? ДА/НЕТ')
while True:
    response = input('> ').upper()
    if not (response.startswith('Д') or response.startswith('Н')):
        print(p2Name + ', please enter "ДА" or "НЕТ".')
    else:
        break

firstBox = 'RED '  # Note the space after the "D".
secondBox = 'GOLD'

if response.startswith('Д'):
    carrotInFirstBox = not carrotInFirstBox
    firstBox, secondBox = secondBox, firstBox

print('''HERE ARE THE TWO BOXES:
  __________     __________
 /         /|   /         /|
+---------+ |  +---------+ |
|   {}  | |  |   {}  | |
|   BOX   | /  |   BOX   | /
+---------+/   +---------+/'''.format(firstBox, secondBox))
print(playerNames)

input('Нажмите Enter, чтобы определить победителя...')
print()

if carrotInFirstBox:
    print('''
   ___VV____      _________
  |   VV    |    |         |
  |   VV    |    |         |
  |___||____|    |_________|
 /    ||   /|   /         /|
+---------+ |  +---------+ |
|   {}  | |  |   {}  | |
|   BOX   | /  |   BOX   | /
+---------+/   +---------+/'''.format(firstBox, secondBox))

else:
    print('''
   _________      ___VV____
  |         |    |   VV    |
  |         |    |   VV    |
  |_________|    |___||____|
 /         /|   /    ||   /|
+---------+ |  +---------+ |
|   {}  | |  |   {}  | |
|   BOX   | /  |   BOX   | /
+---------+/   +---------+/'''.format(firstBox, secondBox))

print(playerNames)

# This modification made possible through the 'carrotInFirstBox variable
if carrotInFirstBox:
    print(p1Name + ' является победителем!')
else:
    print(p2Name + ' является победителем!')

print('Спасибо за игру!')
