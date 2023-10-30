




import datetime

# Задаём константы
DAYS = ('Воскресенье', 'Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятници', 'Суббота')
MONTHS = ('Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь')

print('Calendar Maker, by Al Sweigart al@inventwithpython.com')

while True: # Цикл для запроса у пользователя года.
    print('Введите год календаря:')
    response = input('> ')

    if response.isdecimal() and int(response) > 0:
        year = int(response)
        break

    print('Пожалуйста введите номер года как 2023.')
    continue

while True: # Цикл для запроса у пользователя месяца.
    print('Введите год календаря:')
    response = input('> ')

    if not response.isdecimal():
        print('Пожалуйста введите номер месяца  - 3 для Марта.')
        continue

    month = int(response)
    if 1 <= month <= 12:
        break

    print('Пожалуйста введите номер от 1 до 12')


def getCalendarFor(year, month):
    calText = '' # calText содержит строковое значение с календарём.

    # Размещаем месяц и год вверху календаря:
    calText += (' ' * 34) + MONTHS[month - 1] + ' ' +str(year) + '\n'

    # Добавляем в календарь метки дней недели:
    #
    calText += '...Вс........Пн........Вт........Ср.........Чт..........Пт........Сб........\n'

    # Горизонтальная линия - разделитель недель:
    weekSeparator = ('+----------' * 7) + '+\n'

    # Пустые строки содержат по десять пробелов между разделителями дней |:
    blankRow = ('|          ' * 7) + '|\n'

    # Получаем первую дату месяца. 
    currentDate = datetime.date(year, month, 1)

    # Отнимаем от currentDate по дню, пока не дойдём до воскресенья.
    # (weekday() возвращает для воскресенья 6, а не 0.)
    while currentDate.weekday() != 6:
        currentDate -= datetime.timedelta(days=1)

    while True: # Проходим в цикле по всем неделям в месяце.
        calText += weekSeparator

        #dayNumberRow - строка с метками номеров дней:
        dayNumberRow = ''
        for i in range(7):
            dayNumberLabel = str(currentDate.day).rjust(2)
            dayNumberRow += '|' + dayNumberLabel + (' ' * 8)
            currentDate += datetime.timedelta(days=1) # Переходим к следующему дню.

        dayNumberRow += '|\n' # Добавляем вертикальную линию после субботы.
        # Добавляем в текст календаря строку с номерами дней и 3 пустых строки.
        calText += dayNumberRow
        for i in range(3):
            calText += blankRow

        # Проверяем, закончили ли мы обработку месяца:
        if currentDate.month != month:
            break

    # Добавляем горизонтальную линию в самом низу календаря.
    calText += weekSeparator
    return calText


calText = getCalendarFor(year, month)
print(calText) # Выводим календарь.

# Сохраняем календарь в текстовом файле:
calendarFilename = 'calendar_{}_{}.txt'.format(year, month)
with open(calendarFilename, 'w') as fileObj:
    fileObj.write(calText)

print('Saved to ' + calendarFilename)   