#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import random


# 21. Вывести все числа от 0 до 1000, которые содержат в
# себе цифры 1 и 7. Т.е. числа: 17, 71, 107, 117, 127, 137, …


def find_numbers():
    """
    Input:
    nothing, it have everything it need.
    
    Output:
    numbers which contains 1 and 7
    """
    n = 0
    found_numbers = []
    
    while n < 1000:
        digits = []
        digit_12 = n//10
        digits.append(digit_12//10)
        digits.append(digit_12 % 10)
        digits.append(n % 10)

        have_one = False
        have_seven = False

        for d in digits:
            if d == 1:
                have_one = True
            elif d == 7:
                have_seven = True

        if have_one and have_seven:
            found_numbers.append(n)
            
        n += 1
        
    return found_numbers


# 22. Вывести сумму всех чисел, которые являются степенью 3ки и
# принадлежат диапазону чисел от 0 до 1000000. Т.е. sum = 3^0 + 3^1 + 3^2 + ...


def power3_sum_1method(n=1000000):
    """
    Input:
    n: int() type, upper bound
    
    Output:
    sum: summ of all numbers which is power of 3
    and fit in between 0 and upper bound
    """
    num_of_elements = int(math.log(n, 3))
    sum = 0
    for i in range(num_of_elements + 1):
        a = 3**i
        sum += a
    return sum


def power3_sum_2method():
    """
    Input:
    nothing, it have everything it needs.
    
    Output:
    sum: summ of all numbers which is power of 3
    and fit in between 0 and upper bound == 1000000
    """
    k = 0
    sum = 0
    while True:
        a = 3**k
        k += 1
        if a < 1000000:
            sum += a
        else:
            break

    return sum


def power3_sum_3method():
    """
    Input:
    nothing, it have everything it needs.
    
    Output:
    sum: summ of all numbers which is power of 3
    and fit in between 0 and upper bound == 1000000
    """
    k = 0
    a = 3**k
    sum = 0
    while a < 1000000:
        sum += a
        k += 1
        a = 3**k

    return sum


# 23. Создать функцию, выводящую на экран случайно сгенерированное
# 12 ти-значное натуральное число и возвращающую его наибольшую цифру.


def gen_random_1method(ndigit=12):
    """
    Input:
    ndigit: is lenght in digits of randomly generated number
    
    Output:
    max digit of n-digit number, which is randomly generated.
    """
    twelve_digit = random.randrange(10**(ndigit-1), 10**ndigit)
    td_list = list(str(twelve_digit))
    return twelve_digit, int(max(td_list))


def gen_random_2method(ndigit=12):
    """
    Input:
    ndigit: is lenght in digits of randomly generated number
    
    Output:
    max digit of n-digit number, which is randomly generated.
    """
    k = 0
    max_digit = 0
    twelve_digit = ""
    while k < ndigit:
        rnd_digit = random.randint(0, 9)
        if rnd_digit > max_digit:
            max_digit = rnd_digit
            
        twelve_digit += str(rnd_digit)
        k += 1

    return int(twelve_digit), max_digit


# 24. Случайным образом программа выбирает целое число от 1 до 10 и
# предлагает пользователю его угадать. Пользователь вводит число,
# а программа проверяет его и, если пользователь не угадал,
# то говорит больше или меньше. После чего опять просит угадать.
# И так пока пользователь не угадает выбранное число.


def guess_the_number():
    """
    Guess the number and you will be hailed as the greatest mind! Im jocking :)
    Guess the Number is a fun educational game that challenges you to find a
    number based on greater than or less than feedback.
    """
    print("Hola! What is your name?")
    fellow_name = input("Name: ")
    rnd_number = random.randint(0, 10)
    print(fellow_name + ", I made a number from 0 to 10")

    steps = 0
    guess = -1
    while guess != rnd_number:
        guess = int(input("Guess: "))

        if guess < rnd_number:
            print("Too low")

        if guess > rnd_number:
            print("Too hight")

        steps += 1

    print("Alright, %s you guessed my number. And at the same time used just %i steps." % (fellow_name, steps))
