"""Шифр Цезаря.
Шифр Цезаря - шифр сдвига, в котором шифрование и дешифрование букв
производится путём сложения и вычитания соответствующих чисел.
Дополнительная информация :
Код размещён на 
Теги: короткая, для начинающих, криптография, математическая"""

try:
    import pyperclip # pyperclip копирует текст в буфер обмена.
except ImportError:
    pass # Если библиотека pyperclip не установлена, ничего не делаем.

# Все возможные символы для шифрования / дешифровки:
# (!) Можно добавить также символы для цифр и знаков препинания,
# чтобы шифровать и их.
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print('Шифр Цезаря')
print('Шифр Цезаря шифрует письма, сдвигая их ')
print('на номер ключа. Например, ключ, равный 2, означает, что буква A')
print('зашифрована в C, буква B зашифрована в D и так далее.')
print()

# Спрашиваем у пользователя, хочет он шифровать или расшифровывать:
while True: # Повторяем вопрос, пока пользователь не введёт e или d.
    print('Do you want to (e)ncrypt or (d)ecrypt?')
    response = input('> ').lower()
    if response.startswith('e'):
        mode = 'encrypt'
        break
    elif response.startswith('d'):
        mode = 'decrypt'
        break
    print('Пожалуйста введите букву e или d.')

# Просим пользователя ввести ключ шифрования
while True:
    maxKey = len(SYMBOLS) - 1
    print('Пожалуйста введите ключ (от 0 до {}).'.format(maxKey))
    response = input('> ').upper()
    if not response.isdecimal():
        continue

    if 0 <= int(response) < len(SYMBOLS):
        key = int(response)
        break

# Просим пользователя ввести сообщение для шифровани / расшифровки:
print('Введите сообщение для {}.'.format(mode))
message = input('> ')

# Работаем только с символами в верхнем регисте
message = message.upper()

# Для хранения зашифрованного / расшифрованного варианта сообщения:
translated = ''

# Зашифровываем / расшифровываем каждый символ сообщения:
for symbol in message:
    if symbol in SYMBOLS:
        # Получаем зашифрованное (расшифрованное) числовое значение символа.
        num = SYMBOLS.find(symbol) # Получаем числовое значение символа
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key

        # Производим переход по кругу, если число больше длины SYMBOLS
        # или меньше 0:
        if num >= len(SYMBOLS):
            num = num - len(SYMBOLS)
        elif num < 0:
            num = num + len(SYMBOLS)
        # Добвляем соответствующий числу зашифрованный / расшифрованный символ
        # в translated
        translated = translated + SYMBOLS[num]
    else:
        # Просто добавляем символ без шифрования / расшифровки:
        translated = translated + symbol

# Выводим зашифрованную / расшифрованную строку на экран:
print(translated)

try:
    pyperclip.copy(translated)
    print('Записали {}ed текст в буфер обмена.'.format(mode))
except:
    pass # Если pyperclip не установлен, ничего не делаем.