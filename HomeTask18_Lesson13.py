"""
    Создать текстовый файл, записать в него, построчно, данные которые вводит пользователь.
    Окончанием ввода служит пустая строка.
    Каждая введённая строка, в файле, должна начинаться с новой строки.
"""
print('\tWrite a comment')
with open('text.txt', 'w') as user_text:
    while True:
        input_text = input(': ')
        if input_text == '':
            break
        user_text.write(input_text+'\n')