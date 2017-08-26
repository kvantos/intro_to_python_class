#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime

"""
37. Реализовать магазин, который продает 3 вида товара.
Программа должна показывать, сколько осталось в магазине
каждого товара и какова прибыль на текущий момент продавца
по каждому товару и всего (Прибыль = доход - себестоимость товара).
"""

class RetailShop:
    """
    Super mega retail shop
    """

    __invoice_number = 1
    
    def __init__(self):
        self.total_income = 0
        self.storage_facilities = None
        self.invoices = []
        self.customers = []

    def __str__(self):
        items_dict = {}
        if self.storage_facilities:
            for item in self.storage_facilities.get_items():
                items_dict[item.category] = items_dict.get(item.category, 0) + 1

        invoice_dict = {}
        for invoice in self.invoices:
            invoice_dict[invoice.product.category] = invoice_dict.get(invoice.product.category, 0) + invoice.income

        output = ""
        output += "Customers: %i\n" % len(self.customers)
        output += "Total income: %i\n" % self.total_income
        output += "Income per category:\n"
        for inv in invoice_dict:
            output += "    %s: %i\n" % (inv, invoice_dict[inv])
        output += "Goods left:\n"
        for item in items_dict:
            output += "    %s: %i\n" % (item, items_dict[item])
        
        return output
        
    def set_store(self, store):
        self.storage_facilities = store

    def add_custromer(self, customer):
        self.customers.append(customer)

    def add_invoice(self, invoice):
        self.invoices.append(invoice)
        
    def sel(self, customer_id, item_id):
#        in_number = len(self.invoices) + 1
        items = self.storage_facilities.get_items()
        invoice = Invoice(self.customers[customer_id], items[item_id])
        self.add_invoice(invoice)
        self.total_income += invoice.income
        self.storage_facilities.rm_item(items[item_id])


class Customer:
    """
    Common or garden customer
    """
    def __init__(self, login, email):
        self.login = login
        self.email = email
    

class Invoice:
    """
    A list of goods sent, with a statement of the sum due for these.
    """

    ADDED_VALUE = 20  # in percent
    __invoice_number = 1
    
    def __init__(self, customer, product):
        Invoice.__invoice_number += 1
        self.customer = customer
        self.product = product
        self.cost_price = product.cost_price
        self.date = datetime.datetime.now()
        self.price = (self.cost_price * Invoice.ADDED_VALUE/100) + self.cost_price
        self.income = self.price - self.cost_price


class Store:
    """
    Accumulate products.
    """
    def __init__(self, location, operating_hours, space):
        self.location = location
        self.operating_hours = operating_hours
        self.space = space
        self._items = []

    def __str__(self):
        return "%i %s" % (len(self._items), str(self._items))
    
    def add_items(self, items):
        self._items.extend(items)

    def get_items(self):
        return self._items

    def rm_item(self, item):
        self._items.remove(item)


class Product:
    """
    Father of all assortment
    """
    def __init__(self, category, cost_price, brand, title):
        self.cost_price = cost_price
        # clothing, books, hobby
        self.category = category
        self.brand = brand
        self.title = title
        

class Clothing(Product):
    """
    Category clothing.
    """
    
    def __init__(self, brand, cost_price, size, gender, title):
        super().__init__("clothing", cost_price, brand, title)
        self.size = size
        self.gender = gender


class Book(Product):
    """
    Category for books
    """

    def __init__(self, brand, cost_price, authors, title):
        super().__init__("books", cost_price, brand, title)
        self.authors = authors


class Hobby(Product):
    """
    Various hobby staff
    """

    def __init__(self, brand, cost_price, title):
        super().__init__("hobby", cost_price, brand, title)



