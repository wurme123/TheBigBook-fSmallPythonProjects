




import random, sys

print('''
Введите, какой вид и сколько кубиков нужно бросить. Формат - это количество
кубиков, за которым следует буква "d", за которой следует количество сторон, которые имеют кубики.
Вы также можете добавить корректировку "плюс" или "минус".

Примеры:
    3d6 бросает три 6-гранных кубика
    1d10+2 бросает один 10-гранный кубик и добавляет 2
    2d38-1 бросает два 38-гранных кубика и вычитает 1
    QUIT завершает работу программы
''')


while True: # Основной цикл программы:
    try:
        diceStr = input('> ') # Приглашение ввести описание игральных костей.
        if diceStr.upper() == 'QUIT':
            print('Thanks for playing!')
            sys.exit()

        # Очищаем строку описания игральных костей:
        diceStr = diceStr.lower().replace(' ', '')

        # Ищем "d" в строке описания игральных костей
        dIndex = diceStr.find('d')
        if dIndex == -1:
            raise Exception('Missing the "d" character')

        # Выясняем количество костей. ("3" в "3d6+1")
        numberOfDice = diceStr[:dIndex]
        if not numberOfDice.isdecimal():
            raise Exception('Missing the number of dice.')
        numberOfDice = int(numberOfDice)

        # Выясняем, присутствует ли модификатор в виде знака "+" или "-"
        modIndex = diceStr.find('+')
        if modIndex == -1:
            modIndex = diceStr.find('-')

        # Выясняем количество граней ("6" в "3d6+1")
        if modIndex == -1:
            numberOfSides = diceStr[dIndex + 1 :]
        else:
            numberOfSides = diceStr[dIndex + 1 : modIndex]
        if not numberOfSides.isdecimal():
            raise Exception('Missing the number of sides.')
        numberOfSides = int(numberOfSides)

        # Выяняем числовое значение модификатора ("1" в "3d6+1")
        if modIndex == -1:
            modAmound = 0
        else:
            modAmound = int(diceStr[modIndex + 1 :])
            if diceStr[modIndex] == '-':
                # Меняем числовое значение модификатора на отрицательное
                modAmound = -modAmound

        # Моделируем бросок игральных костей:
        rolls = []
        for i in range(numberOfDice):
            rollResult = random.randint(1, numberOfSides)
            rolls.append(rollResult)

        # Отображаем итоговую сумму очков:
        print('Итого:', sum(rolls) + modAmound, '(Каждый кубик:', end='')

        # Отображаем отдельные броски:
        for i, roll in enumerate(rolls):
            rolls[i] = str(roll)
        print(', '.join(rolls), end='')

        # Отображаем числовое значение модификатора:
        if modAmound != 0:
            modSing = diceStr[modIndex]
            print(', {}{}'.format(modSing, abs(modAmound)), end='')
        print(')')

    except Exception as exc:
        # Перехватываем все исключения и отображаем сообщение пользователя:
        print('Invalid input. Enter something like "3d6" or "1d10+2".')
        print('Input was invalid because: ' + str(exc))
        continue # Возвращаемся к приглашению ввести описание игральных костей