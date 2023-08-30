# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение дробей.
# Для проверки своего кода используйте модуль fractions.

from fractions import *
from math import gcd


def fraction_sum(fraction1, fraction2):
    numerator1, denominator1 = map(int, fraction1.split('/'))
    numerator2, denominator2 = map(int, fraction2.split('/'))
    common_denominator = denominator1 * denominator2
    sum_numerator = numerator1 * denominator2 + numerator2 * denominator1
    gcd_num = gcd(sum_numerator, common_denominator)
    sum_numerator = int(sum_numerator / gcd_num)
    common_denominator = int(common_denominator / gcd_num)
    return f"{sum_numerator}/{common_denominator}"


def fraction_multiplication(fraction1, fraction2):
    numerator1, denominator1 = map(int, fraction1.split('/'))
    numerator2, denominator2 = map(int, fraction2.split('/'))
    product_numerator = numerator1 * numerator2
    product_denominator = denominator1 * denominator2
    gcd_num = gcd(product_numerator, product_denominator)
    product_numerator = int(product_numerator / gcd_num)
    product_denominator = int(product_denominator / gcd_num)
    return f"{product_numerator}/{product_denominator}"


fraction1 = input('Введите первую дробь через слэш "/": ')
fraction2 = input('Введите вторую дробь через слэш "/": ')

sum_fraction = fraction_sum(fraction1, fraction2)
product_fraction = fraction_multiplication(fraction1, fraction2)

check_sum = Fraction(fraction1) + Fraction(fraction2)
check_product = Fraction(fraction1) * Fraction(fraction2)

print('Сумма дробей:', sum_fraction + '. Результат проверки: ', check_sum)
print('Произведение дробей:', product_fraction + '. Результат проверки: ', check_product)

