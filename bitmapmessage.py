"""Сообщение в виде битовой карты, by Al Sweigart al@inventwithpython.com
Отображает текстовое сообщение в соответствии с указанной битовой картой.
Код размещён на https://nostarch.com/big-book-small-python-programming
Tags: крошечная, для начинающих, графика"""

import sys

# (!) Try changing this multiline string to any image you like:

# There are 68 periods along the top and bottom of this string:
# (You can also copy and paste this string from
# https://inventwithpython.com/bitmapworld.txt)
bitmap = """
....................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
...................................................................."""

print('Bitmap Message, by Al Sweigart al@inventwithpython.com')
print('Enter the message to display with the bitmap.')
message = input('> ')
if message == '':
    sys.exit()

# Проходим в цикле по всем строкам битовой карты:
for line in bitmap.splitlines():
    # Проходим в цикле по всем символам строки:
    for i, bit in enumerate(line):
        if bit == ' ':
            # Выводим пустое пространство согласно пробелу в битовой карты:
            print(' ', end='')
        else:
            # Выводим символ сообщения:
            print(message[i % len(message)], end='')
    print()  # Выводим символ новой строки.
