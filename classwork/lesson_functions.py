import numpy as np

name = "jeff bezos"
x = ""
for i in name.split():
    x += i.capitalize()
    x += " "

print(x)


def mypow(a, b):
    return a**b


def rect_square(h, w):
    return h*w


def sq_square(a):
    return rect_square(a, a)


def p_delim(rep=10):
    print("-"*rep)


def p_print(val):
    p_delim()
    print("value: %.2f" % val)
    p_delim(20)


def sq_circle(radius):
    return np.pi*radius**2


def add_multy(a, b):
    sum = a + b
    mult = a*b

    return sum, mult


def empty_funct():
    pass


def cels2far(deg):
    return deg * 1.8 + 32

haha = cels2far(231)
