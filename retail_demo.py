#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from A11 import RetailShop
from A11 import Store
from A11 import Customer
from A11 import Clothing
from A11 import Book
from A11 import Hobby


def cmd():
    
    print("Please select customer to who you want to sell product:")
    for i, customer in enumerate(my_retail.customers):
        print("%i: %s" % (i, customer.login))

    customer_id = int(input("customer > "))

    print("Please select product you want to sell:")
    for i, product in enumerate(my_retail.storage_facilities.get_items()):
        print("%i: %s - %s - %s" % (i, product.category, product.brand, product.title))

    product_id = int(input("product > "))

    try:
        my_retail.sel(customer_id, product_id)
    except RetailShop.OutOfGoods as msg:
        print("=====>> %s" % msg)


my_retail = RetailShop()
print(my_retail)

t_shirt1 = Clothing("Nike", 10, "M", "m", "T-Shirt")
t_shirt2 = Clothing("Madoc", 70, "S", "f", "T-Shirt")
book = Book("Addison-Wesley", 20, "Josee Lajoie,Stanley B. Lippman", "C++ Primer")
hammer = Hobby("Stanley", 15, "Super Hammer")
store_moldavanka = Store("Staroportofrankovskaia, 45", "9:30,19:00", 100)

store_moldavanka.add_items([t_shirt1, t_shirt2, t_shirt2, t_shirt2, book, hammer, hammer, hammer])
my_retail.set_store(store_moldavanka)

customer1 = Customer("tanenbaum", "andrew@gmail.com")
customer2 = Customer("Rochkind", "mark@mail.com")
my_retail.add_custromer(customer1)
my_retail.add_custromer(customer2)


while True:
    print(my_retail)
    cmd()

# print(my_retail)
# cmd()
# print(my_retail)
