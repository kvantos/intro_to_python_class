#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 1. Написать функцию, которая разворачивает строку: abcdefgh -> hgfedcba


def revers_str(input_string):
    """
    Input:
    
    input_string is str() type sequence

    Output:

    reversed input_string by str() type
    """

    return input_string[::-1]


# 2. Написать строковую функции, которая получает два параметра: строку и
# букву html-тега. Функция должна возвращать слово выделенное указанным тегом.
# Например solution("This is <i>test</i> example", "i")  -> "test"


def parse_html(input_string, tag_name):
    """
    Input:
    
    input_string is str() type, html sequence
    tag_name is str() type, name of tag by which extract word

    Output:

    converted input_string from python_style to CamelCase by str() type
    """

    for i in range(len(input_string)):
        ss = input_string.find("<")
        if input_string[ss + 1] == tag_name and input_string[ss + 2] == ">" :
        	# we found opening tag
        	input_string

    return None
        
# 3. Convert a given var name from python_style into CamelizedStyle
# solution("this_is_var_name")  -> "ThisIsVarName"


def underscore_to_cc(input_string):
    """
    Input:
    
    input_string is str() type sequence in python style

    Output:

    converted input_string from python_style to CamelCase by str() type
    """

    cc_str = input_string.title().split("_")
    return "".join(cc_str)


# 4. Задача написать функцию, которая определяет надо ли переводить время
# на час вперед/назад. Должна вернуть +1, если надо переводить вперед, -1,
# если назад, 0 - если не надо. Получает месяц, день недели, день месяца:
# def daylight_saving (month, week_day, day_of_month)


def daylight_saving(m, wd, d):
    """
    Assuming that DST start at last Sunday of March
    DST end at last Sunday of October

    Input:
    
    m: month, wd: week day, d: day of month are int() type
    month, week day and day of month count start from 1

    Output:

    1 if clock need to shift 1 hour forward
    -1 if clock need to shift 1 hour backward
    0 does not need to adjust clock
    """

    if m == 3:
        if wd == 7:
            if 31 >= d > 24:
                return 1

    elif m == 10:
        if wd == 7:
            if 31 >= d > 24:
                return -1

    else:
        return 0


# 5. *Написать функцию, которая разворачивает строку: abcdefgh -> hgfedcba.
# На этот раз без использования циклов и срезов :).


def revers_str2method(input_string):
    """
    Input:

    input_string is str() type sequence

    Output:

    reversed input_string by str() type
    """

    lstr = list(input_string)
    lstr.reverse()
    return "".join(lstr)


def revers_str3method(input_string):
    """
    Input:

    input_string is str() type sequence

    Output:

    reversed input_string by str() type
    """

    r_str_obj = reversed(input_string)
    return "".join(r_str_obj)

# 6. Take two lists, say for example these two:
#  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains
# only the elements that are common between the lists (without duplicates).
# Make sure your program works on two lists of different sizes.


def mix_lists(list1, list2):
    """
    Input:

    two common-or-garden lists by list() type

    Output:

    intersection of two input lists by list() type
    """
    data1 = set(list1)
    data2 = set(list2)

    return list(data1.intersection(data2))


# 7. Write a Python program to remove duplicates from a list.


def rr_duplicates(input_list):
    """
    Input:
    
    list by list() type

    Output:

    list without duplicates by list() type
    """

    return list(set(input_list))
