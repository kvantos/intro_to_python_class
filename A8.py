#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pickle


"""
В программе phone_book
(https://github.com/dbradul/python/blob/master/phone_book.py)
реализовать следующие функции:
* find_entry_age_phonebook # найти все записи с указанным возрастом 
* print_phonebook_by_age   # распечатать все записи 
  отсортированные по возрасту 
* delete_entry_name_phonebook   # найти все записи с указанным именем 
* print_avr_age     # распечатать средний возраст всех абонентов 
* increase_age      # увеличить возраст всем абонентам 
  на заданное пользователем кол-во лет 
* <ваша_функция>  # добавить любую функцию, 
  манипулирующую записями (печать, добавление, удаление) 
  в телефонной книге на ваше усмотрение. 
* добавить поддержку еще одного поля 
  (например, скайп, адрес, день рождения) и сделайте по нему поиск и печать. 
  Т.е. добавить функцию для поиска и обновить существующую функцию печати. 

При выполнении обратите внимание на обработку ошибок. Например,
если при удалении записи с заданным именем нет,
то вывести сообщение “Not found!”.
"""

keep_going = True
phone_book = [
              {"name": "Petr", "surname": "Petrov", "age": 50, "phone_number": "+380501234567"},
              {"name": "Ivan", "surname": "Ivanov", "age": 15, "phone_number": "+380507654321"},
             ]


def is_blank(string):
    if string:
        # string is not None AND string is not empty or blank
        return False
    # string is None OR string is empty or blank
    return True


def print_entry(number, entry):
    print("--[ %s ]--------------------------" % number)
    print("| Surname: %20s |" % entry["surname"])
    print("| Name:    %20s |" % entry["name"])
    print("| Age:     %20s |" % entry["age"])
    if "email" in entry.keys():
        print("| Email:  %20s |" % entry["email"])
    if "phone_number" in entry.keys():
        print("| Phone:  %20s |" % entry['phone_number'])
    print()


def print_phonebook():
    print()
    print()
    print("#########  Phone book  ##########")
    print()

    number = 1
    for entry in phone_book:
        print_entry(number, entry)
        number += 1


def print_phonebook_by_age():
    phone_book_srt = sorted(phone_book, key=lambda person: person['age'])
    idx = 1
    for person in phone_book_srt:
        print_entry(idx, person)
        idx += 1


def add_entry_phonebook():
    surname = str(input("    Enter surname: "))
    name = str(input("    Enter name: "))
    age = int(input("    Enter age: "))
    email = str(input("    Enter EMail: "))

    entry = {}
    entry["surname"] = surname
    entry["name"] = name
    entry["age"] = age
    if not is_blank(email):
        entry["email"] = email
    phone_book.append(entry)

   
def printError(message):
    print("ERROR: %s" % message)


def printInfo(message):
    print("INFO: %s" % message)


def find_entry_name_phonebook(name):
    name = str(input("    Enter name: "))
    
    idx = 1
    found = False
    for entry in phone_book:
        if entry["name"] == name:
            print_entry(idx, entry)
            idx += 1
            found = True
    if not found:
        printError("Not found!!")


def find_entry_age_phonebook():
    age = int(input("    Enter age: "))
    
    idx = 1
    found = False
    for person in phone_book:
        if person['age'] == age:
            print_entry(idx, person)
            idx += 1
            found = True
    if not found:
        printError("O_o There are no users in the phone book with age %i" % age)


def find_by_email():
    email = input("    Enter email: ")
    
    idx = 1
    found = False
    for person in phone_book:
        if 'email' in person.keys() and person['email'] == email:
            print_entry(idx, person)
            idx += 1
            found = True
    if not found:
        printError("O_o There are no users in the phone book with email %s" % email)


def update_phone():
    global phone_book
    name = input("    Enter person name: ")
    phone = input("    Enter phone number: ")

    found_users = list(filter(lambda user: user['name'] == name, phone_book))

    if len(found_users) > 1:
        print("I found more than one user with same name. "
              + "Please choose correct one by input ID number. "
              + "ID number in [] brakets.")
        idx = 0
        for person in found_users:
            print_entry(idx, person)
            idx += 1

        person_id = int(input("    Enter person ID: "))
        if person_id in range(len(found_users)):
            found_users[person_id]['phone_number'] = phone
        else:
            print("You typed wrong ID, try again.")
        
    elif len(found_users) == 1:
        found_users[0]['phone_number'] = phone
    else:
        printError("O_o There are no users in the phone book with name %s" % name)


def delete_entry_name_phonebook():
    global phone_book
    name = str(input("    Enter name: "))
    len_before = len(phone_book)
    phone_book = list(filter(lambda user: user['name'] != name, phone_book))
    len_after = len(phone_book)
    
    if len_before == len_after:
        printError("O_o There are no user in the phone book with name %s" % name)
    

def count_all_entries_in_phonebook():
    print("Total number of entries: ", len(phone_book))


def print_avr_age():
    avg_age = sum(list(map(lambda x: x['age'], phone_book)))/len(phone_book)
    print("Average age of all persons in phonebook is: %i" % avg_age)


def increase_age():
    global phone_book
    nmbrs_of_years = int(input("    Enter number of years to add to current ages: "))
    for person in phone_book:
        person['age'] += nmbrs_of_years
    

def save_to_file():
    pickle.dump(phone_book, open("phone_book.save", "wb"))
    printInfo("Phonebook is saved into 'phone_book.save'")


def load_from_file():
    global phone_book
    phone_book = pickle.load(open("phone_book.save", "rb"))
    printInfo("Phonebook is loaded from 'phone_book.save'")


def print_help():
    print()
    print()
    print()
    print("Select one of actions below:")
    print("     1 - Print phonebook entries")
    print("     2 - Print phonebook entries (by age)")
    print("     3 - Add new entry")
    print("     4 - Find entry by name")
    print("     5 - Find entry by age")
    print("     6 - Find entry by Email")
    print("     7 - Delete entry by name")
    print("     8 - The number of entries in the phonebook")
    print("     9 - Avr. age of all persons")
    print("     10 - Increase age by num. of years")
    print("     11 - Update or add phone number for person")
    print("-----------------------------")
    print("     s - Save to file")
    print("     l - Load from file")
    print("     q - Exit")


def quit_phonebook():
    global keep_going
    print("Bye! See ya next time.")
    keep_going = False


def main():
    global keep_going
    print("(_PhoneBook_)")
    print("Type 'h' for help")
          
    while keep_going:
        try:
            
            commands = {"1": print_phonebook,
                        "2": print_phonebook_by_age,
                        "3": add_entry_phonebook,
                        "4": find_entry_name_phonebook,
                        "5": find_entry_age_phonebook,
                        "6": find_by_email,
                        "7": delete_entry_name_phonebook,
                        "8": count_all_entries_in_phonebook,
                        "9": print_avr_age,
                        "10": increase_age,
                        "11": update_phone,
                        "s": save_to_file,
                        "l": load_from_file,
                        "q": quit_phonebook}

            user_input = input("phonebook> ")
            command = user_input
            
            if command in commands.keys():
                commands[command]()
            else:
                print_help()

        except Exception as message:
            printError("Something went wrong. Try again...")


if __name__ == '__main__':
    main()


