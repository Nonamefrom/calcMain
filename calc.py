#
user_input = input('Введите через запятую и пробел: число1, знак(+,-,*,/), число2 ')
str_input = user_input.split(', ')
num1 = int(str_input[0])
sign = str_input[1]
num2 = int(str_input[2])
#строка ниже попытка вывести строку со знаком - не заработало
#print (f'Ответ: {num1} {sign} {num2} = {num1signnum2}')
if sign == '+':
    print (f'Ответ: {num1} {sign} {num2} = {num1 + num2}')
elif sign == '-':
    print (f'Ответ: {num1} {sign} {num2} = {num1 - num2}')
elif sign == '*':
    print (f'Ответ: {num1} {sign} {num2} = {num1 * num2}')
elif sign == '/':
    print (f'Ответ: {num1} {sign} {num2} = {num1 / num2}')
else:
    print('Несоблюдены условия ввода данных!')