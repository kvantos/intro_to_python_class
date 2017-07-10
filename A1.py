#!/usr/bin/env python3

import math

"""
1. Найти результат выражения для произвольных значений a,b,c: a + b * ( c / 2 )
2. Найти результат выражения для произвольных значений a,b: (a^2 + b^2) % 2
3. Найти результат выражения для произвольных значений a,b,c: ( a + b ) / 12 * c % 4 + b
4. Найти результат выражения для произвольных значений a,b,c: (a - b * c ) / ( a + b ) % c
5. Найти результат выражения для произвольных значений a,b,c: | a - b | /( a + b)^3 - cos( c )
6. Найти результат выражения для произвольных значений a,b,c: ( ln( 1 + c ) / -b )^4 + | a |
"""

a = 2
b = 3
c = 42

# ex1
x = a + b*(c/2)
print("ex1 result of computation:", x)

# ex2
d = (a**2 + b**2) % 2
print("ex2 result of computation:", d)

# ex3
e = (a + b)/12 * c % 4 + b
print("ex3 result of computation:", e)

# ex4
f = (a - b*c)/(a + b) % c
print("ex4 result of computation:", f)

# ex5
g = abs(a - b)/(a + b)**3 - math.cos(c)
print("ex4 result of computation:", g)

# ex6
h = (math.log(1 + c)/(-b))**4 + abs(a)
print("ex6 result of computation:", h)
