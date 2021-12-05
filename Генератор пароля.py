import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters ='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_.'
chars = ''
want_more = 'д'
while want_more == 'д':
    if input('Пароль должен содержать прописные буквы? д - да / н - нет \n') == 'д':
        chars += uppercase_letters
    if input('Пароль должен содержать строчные буквы? д - да / н - нет \n') == 'д':
        chars += lowercase_letters
    if input('Пароль должен содержать знаки препинания? д - да / н - нет \n') == 'д':
        chars += punctuation
    if input('Пароль должен содержать цифры? д - да / н - нет \n') == 'д':
        chars += digits
    if input('Исключить из пароля неоднозначные символы? д - да / н - нет \n') == 'д':
        for c in chars:
            if c in 'il1Lo0O':
                chars = chars.replace(c, '')

    for _ in range(int(input('Введите количество необходимых паролей. \n'))):
        print(*random.sample(chars, int(input('Введите длину пароля. \n'))), sep='')
        
    want_more = input('Хотите сгенерировать еще пароли? д - да / н - нет \n')
    if  want_more == 'н':
        break
    


