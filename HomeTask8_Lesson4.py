USER_INPUT = input('Write string: ')
EVEN_CHARS = ''
ODD_CHARS = ''
FIFTH = USER_INPUT[4] if len(USER_INPUT)>5 else None
ALL_TO_10 = USER_INPUT[:10]
LAST_5 = USER_INPUT[-5::]
REVERS = USER_INPUT[::-1]
REVERS_2 = USER_INPUT[::-2]
LENGTH = len(USER_INPUT)
for i in range(len(USER_INPUT)):
    if i%2 == 0:
        EVEN_CHARS += USER_INPUT[i]
    elif i%2 != 0:
        ODD_CHARS += USER_INPUT[i]

print('Все символы \nс четным индексом в строке -', EVEN_CHARS)
print('Все символы \nс нечетным индексом -', ODD_CHARS)
print('Пятый символ в строке -', FIFTH)
print('Все до десятого символа -', ALL_TO_10)
print('Последние 5 символов строки -', LAST_5)
print('Строку в обратном порядке -', REVERS)
print('Строку в обратном \nпорядке через один символ - ', REVERS_2)
print('Длинну строки -', LENGTH)
#Is palindrom
for o in range(len(USER_INPUT)):
    if USER_INPUT[o] != REVERS[o]:
        print('String is not palindrome')
        break
else:
    print('String is palindrome')
