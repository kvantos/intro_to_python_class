#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Test 2
Написать программу для библиотеки, которая ведет учет
выданных на руки книг и газет. Необходимо, чтобы
программа реализовывала следующие функции и ограничения:

5 баллов:
1. на руках у одного человека не может быть одновременно
больше 3х наименований книг и/или газет
2. вывести сколько книг(газет) на руках у конкретного
человека

10 баллов
3. вывести кто больше всего книг(газет) прочел
4. вывести какую книгу(газету) чаще всего берут почитать

15 баллов
5. вывести что больше читают - книги или газеты
"""


class ArchiveError(Exception):
    pass


class LimitExhausted(ArchiveError):
    pass


class ItemNotExists(ArchiveError):
    pass


class Archive:
    def __init__(self):
        self.log = {"book": [], "npaper": [], "customer": []}
        self.usage_log = []

    def __str__(self):
        output = "\n==============\n"
        output += "Archive stats:"
        output += "\n==============\n"
        output += "\nTotal Books: %i" % len(self.log['book'])
        output += "\nTotal Newspapers: %i" % len(self.log['npaper'])
        output += "\nTotal Customers: %i" % len(self.log['customer'])
        output += "\n"

        books_on_hands = [b for b in self.log['book'] if b.in_hand]
        npapers_on_hands = [np for np in self.log['npaper'] if np.in_hand]
        
        output += "Books on hands: %i\n" % len(books_on_hands)
        output += "Newspapers on hands: %i" % len(npapers_on_hands)
        output += "\n"
        
        return output

    def give_item(self, item, customer_id):
        if not item.in_hand:
            self.log['customer'][customer_id].add_item(item)
            item.in_hand = True
            item.usage_counter += 1
            item_type = item.who_am_i
            item_id = self.log[item_type].index(item)
            usage_dict = {"customer": customer_id, "item_type": item_type,
                          "item_id": item_id}
            self.usage_log.append(usage_dict)
        else:
            raise ItemNotExists("This %s took somebody else." % item.who_am_i)

    def take_item(self, item, customer_id):
        self.log['customer'][customer_id].rm_item(item)
        item.in_hand = False

    def add(self, entity):
        self.log[entity[0].who_am_i].extend(entity)

    def get_items(self, item_type):
        return self.log[item_type]


class Customer:
    def __init__(self, name, contact):
        self.who_am_i = "customer"
        self.name = name
        self.contact = contact


class Hand(Customer):

    CAN_KEEP = 3
    
    def __init__(self, name, contact):
        super().__init__(name, contact)
        self.items_in_hand = {"book": [], "npaper": []}
        
    def __str__(self):
        output = ""
        output += "\n----------------\n"
        output += "  %s" % self.name
        output += "\n----------------\n"
        output += "\nBooks: \n"
        for i, book in enumerate(self.items_in_hand['book']):
            output += "%i. " % i + str(book) + "\n"

        output += "\n\nNewspapers: "
        for i, npaper in enumerate(self.items_in_hand['npaper']):
            output += "%i. " % i + str(npaper) + "\n"

        output += "\n"
        return output
    
    def add_item(self, item):
        total_books = len(self.items_in_hand['book'])
        total_npapers = len(self.items_in_hand['npaper'])
        total_items = total_books + total_npapers
        
        if total_items < Hand.CAN_KEEP:
            self.items_in_hand[item.who_am_i].append(item)
        else:
            raise LimitExhausted("%s have %i books and %i newspapers." % (self.name, total_books, total_npapers)
                                 + " Cant keep more than 3 items at same time.")

    def rm_item(self, item):
        if len(self.items_in_hand[item.who_am_i]) < 1:
            raise LimitExhausted("no single %s left, nothing to remove." % item.who_am_i)
        else:
            self.items_in_hand[item.who_am_i].remove(item)
        

class Medium:
    def __init__(self):
        self.in_hand = False


class Book(Medium):

    def __init__(self, title, author, publisher, year):
        super().__init__()
        self.usage_counter = 0
        self.who_am_i = "book"
        self.title = title
        self.author = author
        self.publisher = publisher
        self.year = year

    def __str__(self):
        return "%s, %s" % (self.author, self.title)


class Newspaper(Medium):
    def __init__(self, title, date):
        super().__init__()
        self.usage_counter = 0
        self.who_am_i = "npaper"
        self.title = title
        self.date = date

    def __str__(self):
        return "%s, %s" % (self.date, self.title)
