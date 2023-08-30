# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

def hex_system(num):
    hex_chars = '0123456789abcdef'
    hex_number = ''

    while num > 0:
        div_result = num // 16
        remainder = num % 16
        hex_number = hex_chars[remainder] + hex_number
        num = div_result

    return hex_number


number = int(input('Введите число: '))
hex_num = hex_system(number)
check = hex(number)
check = check[2:]

print(f'Число {number} в 16-ричной системе счисления: {hex_num}.\nРезультат проверки: {check}')
