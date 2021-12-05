import random

print('Добро пожаловать в числовую угадайку')

def is_valid(digit, range):
    return digit.isdigit() and 1 <= int(digit) <= range

counter = 1
guess = 0
again = 'да'

while again.lower() == 'да':
    n = input('Каким может быть максимальное загаданное число? \n')
    if not n.isdigit():
        print('Введите именно целое число, пожалуйста')
        continue


    else:
        x = random.randint(1, int(n))
        guess = input('Предположите, какое число загадано от 1 до указанного вами максимума. \n')
        again = ''

        while guess != x:
            if not is_valid(guess, int(n)):
                guess = input('А может быть все-таки введем целое число от 1 до до указанного вами максимума \n')
                counter += 1

            else:
                guess = int(guess)
                if guess < x:
                    guess = input('Ваше число меньше загаданного, попробуйте еще разок \n')
                    counter += 1
                elif guess > x:
                    guess = input('Ваше число больше загаданного, попробуйте еще разок \n')
                    counter += 1
                else:
                    print('Вы угадали, поздравляем! Количество попыток:', counter)

                    again = input('Хочешь сыграть еще? Напиши "да" \n')

print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
