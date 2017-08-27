import lesson_conditions
import random

for i in range(3):
    print("hello there %i" % i)


for s in range(101):
    if lesson_conditions.is_even(s):
        print(s)

for i in range(1980, 2030):
    if lesson_conditions.is_leap_year(i):
        print(i)

for i in range(100, 201, 2):
    print(i)

ss = "GitHub is a development platform inspired by the way you work. From open source to business, you can host and review code, manage projects, and build software alongside millions of other developers."

for symbol in ss:
    if symbol.isupper():
        print("TT:", symbol)

for symbol in ss:
    if symbol.isprintable() and not symbol.isalnum() and not symbol.isspace():
        print(symbol)

ns = 0

for symbol in ss:
    if symbol.isspace():
        ns += 1

print(ns)

x = 0
for di in range(101):
    x += di

print("x:", x)

h = 0
for i in range(100):
    nm = random.randint(100, 200)
    h += nm

print("total:", h)

