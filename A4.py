#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

# 14. Написать функцию, которая будет проверять четность некоторого числа.


def is_even(input_number):
    """
    Input:
        input_number: common-or-garden Integer number to
        check if it odd or even

    Output:
        True if even, False if odd.
    """

    return not (input_number % 2)


# 15. Написать функцию, которая отвечает на вопрос, пересекаются ли две
# заданные окружности на плоскости. Каждая окружность задается
# координатами центра и радиусом.

def is_cross(x1, y1, x2, y2, r1, r2):
    """
    Input:
        x1,y1: coordinates of center of first circle
        x2,y2: coordinates of center of second circle
        r1,r2: radius of first and second circle respectively

    Output:
        True if two circles cross, False if not.
    """

    cat_a = abs(x1 - x2)
    cat_b = abs(y1 - y2)
    # hypo is distance between centers of circles
    circle_center_dist = math.sqrt(cat_a**2 + cat_b**2)
    circle_dist = circle_center_dist - r1 - r2

    radius_big = max(r1, r2)
    radius_smoll = min(r1, r2)
    
    if circle_dist > 0:
        return False
    
    elif circle_center_dist + radius_smoll < radius_big:
        return False
    
    else:
        return True
    
# 16. Два поезда движутся на скорости V1 и V2 навстречу друг другу.
# Между ними 10 км. пути. Через 4 км пути первый поезд может
# свернуть на запасной путь. При заданных скоростях узнать
# столкнутся ли поезда.


def is_collade(v1, v2):
    """
    Input:
        v1,v2: velocity of train one and train two respectively in km/h

    Output:
        True if trains collade under defined circumstates, False if not
    """

    t1 = 4/v1
    s1 = t1*v2

    if s1 >= 6:
        return True
    else:
        return False
    
# 17. Написать функцию решения квадратного уравнения.


def factoring_quadratic_equation(a, b, c):
    """
    Input:
        a*x**2 + b*x + c = 0

        where x represents an unknown, and a, b, and c represent
        known numbers such that a is not equal to 0. The numbers a,
        b, and c are the coefficients of the equation, and may be
        distinguished by calling them, respectively, the quadratic
        coefficient, the linear coefficient and the constant or free term.

    Output:
        A quadratic equation with real or complex coefficients has two
        solutions, called roots. These two solutions may or may not be
        distinct, and they may or may not be real. In this exercise we
        will work only with real ones.
    """

    if a == 0:
        # If a = 0, then the equation is linear, not quadratic
        return None, None

    D = b**2 - 4*a*c

    if D == 0:
        x = -1*b/(2*a)
        return x, None

    elif D > 0:
        x1 = (-1*b + math.sqrt(D))/(2*a)
        x2 = (-1*b - math.sqrt(D))/(2*a)
        return x1, x2

    else:
        return None, None
