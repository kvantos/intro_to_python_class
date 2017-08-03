#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import A4
import math
import random
import copy
import string

# 25. Вычислить факториал некоторого числа, используя рекурсию.


def factorial(x):
    """
    Input:
    x: some integer number
    
    Output:
    factorial of input number.
    
    """

    fact = 1
    for n in range(1, x+1):
        fact *= n
    
    return fact


print("task 25, resolution for 9")
print("-------------------------")
print(factorial(9))
print("")


def factorial2(x):
    """
    second method with exploating recursion
    """
    if x == 1:
        return 1
    else:
        return x*factorial2(x-1)


print("task 25, recursion method, resolution for 9")
print("-------------------------------------------")
print(factorial2(9))
print("")


# 26. Вывести на экран все простые числа от 1 до 100.


def find_prime_numbers(n=100):
    """
    Input:
    n: the upper bound of the range for which you want to select
       all prime numbers.
    
    Output:
    list of prime numbes
    
    """
    
    prime_numbers = list(range(2, n+1))

    sqn = math.sqrt(n)
    p = 2
    j = 1
    
    while p < sqn:
        
        for i in range(j, len(prime_numbers))[::-1]:
            
            if prime_numbers[i] % p == 0:
                del prime_numbers[i]
                
        p = prime_numbers[j]
        j += 1

    return prime_numbers


print("task 26, prime numbers in range 1 to 100")
print("----------------------------------------")
print(find_prime_numbers())
print("")

# 27. Создайте список на 50 элементов из всех нечётных чисел от 1 до 99,
# выведите его на экран в строку, а затем этот же список выведите на
# экран тоже в строку, но в случайном порядке
# (например, 99 11 43 19 … 7 91 3 1).


def even_print():
    """
    Input:
    Nothing, it have everything it needs
    
    Output:
    Two lists: first one with only odd numbers, second one
    same as first but randomized.
    """

    cool_list = list(range(1, 100))
    
    for i in range(len(cool_list))[::-1]:
        if A4.is_even(cool_list[i]):
            del cool_list[i]

    rnd_list = copy.deepcopy(cool_list)
    random.shuffle(rnd_list)
    print(cool_list)
    print(rnd_list)


print("task 27, generate two lists, straitforward one and randomized")
print("-------------------------------------------------------------")
even_print()
print("")


def even_print2():
    """
    Input:
    Nothing, it have everything it needs
    
    Output:
    Two lists: first one with only odd numbers, second one
    same as first but randomized.
    """

    cool_list = list(range(1, 100, 2))
    rnd_list = cool_list.copy()
    random.shuffle(rnd_list)
    print(cool_list)
    print(rnd_list)


print("task 27, second solution")
print("------------------------")
even_print2()
print("")

# 28. Создайте 2 списка из 5 случайных целых чисел из отрезка [0;5] каждый,
# выведите списки на экран в двух отдельных строках. Посчитайте среднее
# арифметическое элементов каждого списка и сообщите, для какого из списков
# это значение оказалось больше (либо сообщите, что их
# средние арифметические равны).


def gen_rand_lists():
    """
    Generate two lists with random numbers in [0,5], output them and
    compare their mean and tell who is greater
    """
    
    def gen_list():
        ll = []
        for i in range(5):
            ll.append(random.randint(0, 5))

        return ll

    def calc_average(x):
        sum = 0
        for i in x:
            sum += i

        return sum/len(x)
    
    list1 = gen_list()
    list2 = gen_list()

    list1_average = calc_average(list1)
    list2_average = calc_average(list2)

    print("list1:", list1)
    print("list2:", list2)

    if list1_average > list2_average:
        print("Average of list1 is %.2f and bigger than %.2f of list2" % (list1_average, list2_average))
    elif list1_average == list2_average:
        print("Average of list1 %.2f is the same as list2 %.2f" % (list1_average, list2_average))
    else:
        print("Average of list2 is %.2f and bigger than %.2f of list1" % (list2_average, list1_average))
        

print("task 28, generate two lists and compare mean")
print("--------------------------------------------")
gen_rand_lists()
print("")

# 29. Создайте список из 11 случайных целых чисел из отрезка [-1;1],
# выведите список на экран в строку. Определите какой элемент встречается
# в списке чаще всего и выведите об этом сообщение на экран. Если два каких-то
# элемента встречаются одинаковое количество раз, то не выводить ничего.


def count_numbers(n=11):
    """
    Generate list of random digits and calculate max appearence of any.
    """

    number_list = [random.randint(-1, 1) for i in range(n)]
    digits = list(set(number_list))
    number_counts = [number_list.count(i) for i in digits]
    data_store = [digits, number_counts]

    print(number_list)

    if len(set(data_store[1])) == len(data_store[0]):
        max_count = max(data_store[1])
        pos_of_max = data_store[1].index(max_count)
        max_digit = data_store[0][pos_of_max]
        print("%i appeared %i times" % (max_digit, max_count))


print("taks 29, Generate list of random digits")
print("---------------------------------------")
count_numbers()
print("")

# 30. Создать программу, которая запрашивает у пользователя произвольную
# строку символов. Далее программа ее шифрует и выводит на экран в
# зашифрованном виде. Шифрование происходит путем замены каждого
# символа символом, который находится на 5 позиций правее в предопределенной
# таблице шифрования. Таблица шифрования задается программистом в виде
# одномерного списка символов. Если при выборе символа для шифровки таблица
# шифрования заканчивается, то циклически переходить к ее началу.
# * Например: Таблица шифрования (а,б,в,г,д,о,1,2,3,4,5,6,-,0)
# * Исходная строка, которую ввел пользователь: год-2016
# * Зашифрованная строка, которую выдала программа: 354г-д6в
# * Примечание: т.н. таблица шифрования может быть представлена как
#   строка или список.


def encript_string():
    """
    Input:
    user input acii string in command prompt
    
    Output:
    encoded string with super secure encription algorithm
    """

    dictionary = string.ascii_lowercase + string.digits
    # dictionary = 'а,б,в,г,д,о,1,2,3,4,5,6,-,0'.split(",")
    dict_len = len(dictionary)

    print("Hello there, please input string which you want to encript.")
    raw_string = input("type string: ")

    encoded_string = []
    for ch in raw_string:
        ind = dictionary.index(ch) + 5
        if (ind + 1) > dict_len:
            ind = ind - dict_len
            
        encoded_string.append(dictionary[ind])
        
    print("".join(encoded_string))


print("task 30, encript ascii string")
print("-----------------------------")
encript_string()
print("")


# 31. Создать генератор паролей, который будет генерировать случайные
# неповторяющиеся пароли по следующим правилам:
# * Пароль состоит из 8 символов
# * В пароле допускаются только латинские большие и маленькие буквы,
#   цифры и символ подчеркивания
# * Пароль обязательно должен содержать Большие и маленькие буквы и цифры


def pw_gen(pwd_len=8):
    """
    Input: len of password

    Output: random password.
    """

    dict_al = list(string.ascii_lowercase + "_")
    dict_au = list(string.ascii_uppercase + "_")
    dict_d = [str(random.randrange(10)) for d in range(len(dict_al))]

    [random.shuffle(dict) for dict in [dict_al, dict_au]]

    strong_list = []
    for section in zip(dict_al, dict_au, dict_d):
        strong_list.extend(section)

    strong_pwd = strong_list[:pwd_len]
    random.shuffle(strong_pwd)
    
    return "".join(strong_pwd)


print("task 31, generate random password")
print("---------------------------------")
print(pw_gen())
print("")
