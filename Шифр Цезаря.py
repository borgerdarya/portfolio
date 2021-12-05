# Шифр Цезаря - один из наиболее древнейших известных шифров.
# Схема шифрования очень проста — используется сдвиг буквы алфавита на фиксированное число позиций.

def shifr(step, text):
    answer = ''
    for el in text.lower():
        if alphabet.find(el) == -1:
            answer += el
            continue
        elif alphabet.find(el) + step > len(alphabet) - 1:
            answer += alphabet[(alphabet.find(el) + step) - len(alphabet)]
        else:
            answer += alphabet[alphabet.find(el) + step]
    for i in range(len(text)):
        if text[i] in text.upper():
            answer = answer[:i] + answer[i].upper() + answer[i + 1:]
    return answer

def deshifr(step, text):
    answer = ''
    for el in text.lower():
        if alphabet.find(el) == -1:
            answer += el
            continue
        else:
            answer += alphabet[alphabet.find(el) - step]
    for i in range(len(text)):
        if text[i] in text.upper():
            answer = answer[:i] + answer[i].upper() + answer[i + 1:]
    return answer


want_more = '1'
while want_more == '1':
    goal = input('Что вы хотите сделать? 1 - ЗАшифровать, 2 - РАСшифровать \n')
    language = input('Выберите язык. en/ru\n')
    steps = int(input('Введите шаг сдвига \n'))
    textshifr = input('Введите текст \n')

    if language == 'en':
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
    elif language == 'ru':
        alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'


    if goal == '1':
        print(shifr(steps, textshifr))

    if goal == '2':
        print(deshifr(steps, textshifr))

    want_more = input('Хочешь еще поиграть? 1 - да / 2 - нет \n')
    if  want_more == '2':
        break
