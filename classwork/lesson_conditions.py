import math


def dvd(a, b):
    if b != 0:
        return a / b

    else:
        return math.inf


def dvdd(a, b):
    b_is_zero = (b == 0)

    if b_is_zero:
        return a / b

    else:
        return math.inf


def is_zero(v):
    return v == 0


def dvddf(a, b):

    if is_zero(b):
        return math.inf

    else:
        return a / b


def check_letter(le):
    charr = le[0]
    if charr.isupper() and charr.upper() == 'A':
        print("yehoo")

    else:
        print("nothing")


def is_mill(year):
    if year >= 1981 and year <= 2000:
        return True
    else:
        return False


def is_leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True

    else:
        return False

def is_even(ch):
    return not ch % 2
