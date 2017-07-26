#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import A4

# Каждому символу в таблице символов Unicode соответствует число.
# Написать функцию, которая рассчитывает сумму чисел, которые
# соответствуют символам, стоящим между двумя заданными включительно.
# Например, в функцию передаются символы ‘x’ и ‘z’.
# Значит надо вычислить сумму кодов символов ‘x’,’y’,’z’.


def utf_jungle(sym1, sym2):
    """
    Input:
    
    sym1, sym2: symbols, str() type

    Output:

    summ of all symnols in range
    """

    code1 = ord(sym1)
    code2 = ord(sym2)

    hi_code = max(code1, code2)
    low_code = min(code1, code2)

    sum = 0

    for i in range(low_code, hi_code + 1):
        sum += i

    return sum


# Написать функцию для поиска среднего арифметического
# среди 100 случайно сгенерированных чисел.


def average(count=100):
    """
    Input:

    count: count of numbers to be used in calculation of average.

    Output:

    average in random int() numbers
    """

    sum = 0

    for i in range(count):
        random_number = random.randint(0, count)
        sum += random_number

    return sum/count

# Написать функцию для поиска разницы сумм всех четных
# и всех нечетных чисел списка. Т.е. от суммы четныx
# чисел вычесть сумму нечетных чисел в списке.


def crunch_numbers(numbers_list):
    """
    Input:

    list of numbers by list() type

    Output:

    diff between summ of even and summ of odd
    """
    sum_of_even = 0
    sum_of_odd = 0
    
    for i in numbers_list:
        if A4.is_even(i):
            sum_of_even += i
            
        else:
            sum_of_odd += i

    return sum_of_even - sum_of_odd
