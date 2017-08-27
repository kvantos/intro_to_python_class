#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import T2
import sys
from prompt_toolkit import prompt
from prompt_toolkit.contrib.completers import WordCompleter


bird_person = T2.Hand("Bird Person", "bp@gmail.com")
rick = T2.Hand("Rick Sanches", "rs@gmail.com")
morty = T2.Hand("Morty", "mr@gmail.com")

b1 = T2.Book("Coders at Work: Reflections on the Craft of Programming",
             "Peter Seibel", "Apress", 2009)
b2 = T2.Book("Code Complete: A Practical Handbook of Software Construction",
             "Steve McConnell", " Microsoft Press", "2009")
b3 = T2.Book("The Mythical Man Month", "Frederick P. Brooks, Jr. Page",
             "Addison-Wesley Professional", "1995")
b4 = T2.Book("Don’t Make Me Think, Revisited: A Common Sense Approach to Web Usability",
             "Steve Krug", "New Riders", "2014")
b5 = T2.Book("The Pragmatic Programmer: From Journeyman to Master",
             "Andrew Hunt", "Addison-Wesley Professional", "1999")

np1 = T2.Newspaper("The New York Times", "01-23-2017")
np2 = T2.Newspaper("The Wall Street Journal", "05-17-2017")
np3 = T2.Newspaper("Los Angeles Times", "03-10-2017")
np4 = T2.Newspaper("New York Post", "05-05-2017")
np5 = T2.Newspaper("Chicago Tribune", "06-07-2017")

my_archive = T2.Archive()

my_archive.add([bird_person, rick, morty])
my_archive.add([b1, b2, b3, b4, b5])
my_archive.add([np1, np2, np3, np4, np5])


def give():
    print("==============================")
    print("Choice customer from the list:")
    print("==============================")
    customers = {c[1].name: c[0] for c in enumerate(my_archive.get_items('customer'))}
    customers_completer = WordCompleter(customers.keys())
    
    for item in customers.keys():
        print("%s" % item)
    print()
    
    customer = prompt('customer ~> ', completer=customers_completer)
    customer_id = customers[customer]

    print("===========================")
    print("Choice which book you give:")
    print("===========================")
    books = {b.title: b for b in my_archive.get_items('book')}
    books_completer = WordCompleter(books.keys())
    
    for item in books.keys():
        print("%s" % item)
    print()
    
    book = prompt('book ~> ', completer=books_completer)
    
    try:
        my_archive.give_item(books[book], customer_id)
    except Exception as msg:
        print("====>> %s" % msg)


def take():
    pass


def stats():
    print(my_archive)


def customers():
    pass

    
commands = {"stats": stats, "customers": customers, "give": give, "take": take}
commands_completer = WordCompleter(commands.keys())


def help():
    print("Commands available:")
    output = ""
    for c in commands.keys():
        output += str(c) + " "
    print(output)

    
while True:
    try:
        command = prompt('archive ~> ', completer=commands_completer)
        commands[command]()
        
    except (KeyError):
        help()
        
    except (KeyboardInterrupt, EOFError):
        print("\n See ya!")
        sys.exit(0)
                     
