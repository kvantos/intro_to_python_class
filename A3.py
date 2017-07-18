#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


def exercise9(input_string):
    """
    9. Написать программу, которая переводит в верхний регистр второе слово
    (слово - последовательность символов между двумя пробелами).
    Например: "abc def ghj" -> "abc DEF ghj"
    """
    
    words = input_string.split(' ')
    word2up = words[1].upper()
    words[1] = word2up
    
    return " ".join(words)


def exercise10(input_string):
    """
    10. Дана строка вида "Leo Tolstoy*1828-08-28*1910-11-20".
    В этой строке указаны имя писателя и через символ * даты рождения и смерти.
    Даты указаны в формате "YYYY-MM-DD". Требуется написать программу,
    которая по переданной строке определит возраст писателя и
    вернет его имя и возраст. Например, для строки
    "Leo Tolstoy*1828-08-28*1910-11-20" программа должна вернуть:
    "Leo Tolstoy", 82. Месяцы и дни можно игнорировать.
    """

    name, date_birth, date_die = input_string.split('*')
    year_b = int(date_birth.split('-')[0])
    year_d = int(date_die.split('-')[0])

    age = year_d - year_b

    return ("\"%s\", %i" % (name, age))


def exercise11(angle):
    """
    11. Написать функцию, которая будет переводить градусы в радианы.
    Используя эту функцию вывести на экран значения
    косинусов углов в 60, 45 и 40 градусов.
    """
    
    return angle * math.pi / 180


def exercise12(input_digit):
    """
    12. Написать функцию, которая рассчитывает сумму всех цифр
    некоторого трехзначного числа, введенного пользователем в консоли,
    без использования операторов цикла.
    """

    digit1 = input_digit//100
    digit2 = (input_digit % 100)//10
    digit3 = (input_digit % 100) % 10

    return digit1 + digit2 + digit3


def exercise13(cat_a, cat_b):
    """
    13. Пользователь вводит длины катетов прямоугольного треугольника.
    Написать функцию, которая вычислит и выведет на экран площадь
    треугольника и его периметр.
    """

    hypo = math.sqrt(cat_a**2 + cat_b**2)
    triangle_s = cat_a * cat_b / 2
    triangle_p = hypo + cat_a + cat_b
    
    return triangle_s, triangle_p


print("ex9: ", exercise9("abc def ghj"))
print("ex10: ", exercise10("Leo Tolstoy*1828-08-28*1910-11-20"))
print("ex11, cos(60): %.3f" % math.cos(exercise11(60)))
print("ex11, cos(45): %.3f" % math.cos(exercise11(45)))
print("ex11, cos(40): %.3f" % math.cos(exercise11(40)))
print("ex12, 123: %i" % exercise12(123))
print("ex13, for cat 11 and 12, square: %.2f, perimetr: %.2f" % (exercise13(11, 12)))
