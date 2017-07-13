#!/usr/bin/env python3

"""
7. Преобразовать строку с американским форматом даты в европейский.
Например, "05.17.2016" преобразуется в "17.05.2016"

8. Написать программу, которая берет две строки и помещает первую
строку в середину второй. Результат помещается в середину первой.
Длину строки можно получить с помощью функции len().
Для простоты можно считать, что длины строк четные.
"""

# ex7 method 1
us_date = "01.20.1970"

month = us_date[:2]
day = us_date[3:5]
year = us_date[-4:]

eu_date = day + "." + month + "." + year

print("Date in US format %s transformed in to EU format %s"
      % (us_date, eu_date))

# ex7 method 2
us_date = "02.21.1970"

(month, day, year) = us_date.split('.')
eu_date = ("%s.%s.%s" % (day, month, year))

print("Date in US format %s transformed in to EU format %s"
      % (us_date, eu_date))

# ex8
dave = "I shall be forced to disconnect you"
hal9000 = "I was only trying to do what I thought best."

center_of_hal9000 = len(hal9000)//2
step1 = hal9000[:center_of_hal9000] + dave + hal9000[center_of_hal9000:]
print(step1)

center_of_dave = len(dave)//2
step2 = dave[:center_of_dave] + step1 + dave[center_of_dave:]
print(step2)
