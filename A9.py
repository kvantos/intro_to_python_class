#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
from pprint import pprint

"""
33. Для подсчета баллов, набранных студентами группы надо обработать
информацию, представленную в виде взаимосвязанных структур данных:

    * group - список словарей, где словарь описывает информацию о студенте.
    * hw_results: список с информацией о решенных д/з.
      Каждый элемент - это словарь с ключами: id студента,
      task_completion - список выполненных д/з.
    * test1_results: список с информацией о решенном Test1.
      Каждый элемент - это словарь с ключами: id студента,
    * task_completion - список выполненных заданий
    * test1_weights: словарь с весами заданий Test1.
      Ключ - номер задачи, значение - вес задачи
      (кол-во баллов, которое начисляется за ее решение).

Между этими данными связь устанавливается с помощью ключа студента.
Например, студенту с id=1024, соответствуют домашние задания и задачи из Test1,
у которых ключу “id” соответствует значение 1024.
Связь между весом задачи Test1 и ее номером устанавливается по
ключу в словаре test1_weights.

Необходимо написать 2 функции:
    * update_student_results: обновляет рейтинг студента,
      на основании предоставленной информации. См. описание ф-ции.
    * print_student_info: распечатывает информацию о студенте,
      сортируя по указанному ключу из словаря студента.
      По умолчанию сортировка по ключу ‘fullname’.

Данные для обработки:
https://github.com/dbradul/python/blob/master/class_stats.py

Также можно реализовать эту задачу, получив данные через RestAPI.
Пример работы со студентом показан в модуле:
https://github.com/dbradul/python_classes/blob/master/basics/class_stats_v2.py

Примечание:
Формат данных полученных через RestAPI может отличаться. Например,
веса заданий контрольной возвращаются в виде списка, а не словаря,
как в модуле class_stats.py
"""

BASE_URL = "http://54.201.47.219:8080/api"
VERSION = "v1"
URL = "%s/%s" % (BASE_URL, VERSION)
NUM_OF_TESTS = 12


#------------------------------------------------------------------------------
def log_error(msg):
    print("ERROR: ", msg)


#------------------------------------------------------------------------------
def get_students():
    response = requests.get(URL + '/students')
    result = None

    if response.status_code == 200:
        json_object = response.json()
        result = json_object['students']
    else:
        log_error(response.content)

    return result


#------------------------------------------------------------------------------
def get_student(id):
    response = requests.get(URL + '/students/' + str(id))
    result = None

    if response.status_code == 200:
        json_object = response.json()
        result = json_object['student']
    else:
        log_error(response.content)

    return result


#------------------------------------------------------------------------------
def get_hw_results():
    response = requests.get(URL + "/hw_results")
    result = None

    if response.status_code == 200:
        json_object = response.json()
        result = {k['id']: k['task_completion'] for k in json_object}
        
    else:
        log_error(response.content)
        
    return result


#------------------------------------------------------------------------------
def get_test1_results():
    response = requests.get(URL + "/test1_results")
    result = None

    if response.status_code == 200:
        json_object = response.json()
        result = {k['id']: k['task_completion'] for k in json_object}
        
    else:
        log_error(response.content)
        
    return result


#------------------------------------------------------------------------------
def get_test1_weights():
    response = requests.get(URL + "/test1_weights")
    result = None

    if response.status_code == 200:
        json_object = response.json()
    else:
        log_error(response.content)

    result = json_object['test1_weights']
    return result


#------------------------------------------------------------------------------
def update_student(id, upd_fields):
    response = requests.put(URL + '/students/' + str(id),
                            json=json.dumps(upd_fields))

    result = response.status_code == 200

    if not result:
        log_error(response.content)

    return result


#------------------------------------------------------------------------------
def add_student(student):
    response = requests.post(URL + '/students/',
                             json=json.dumps(student))

    result = response.status_code == 200

    if not result:
        log_error(response.content)

    return result


#------------------------------------------------------------------------------
def reset():
    response = requests.put(URL + '/reset')

    result = response.status_code == 200

    if not result:
        log_error(response.content)

    return result


#------------------------------------------------------------------------------
def demo():
    '''
    Demonstrates fetching, updating and adding new student.
    Resets remote DB afterwards
    :return: None
    '''

    # available urls
    # http://54.201.47.219:8080/api/v1/students/
    # http://54.201.47.219:8080/api/v1/students/1025
    # http://54.201.47.219:8080/api/v1/hw_results/
    # http://54.201.47.219:8080/api/v1/hw_results/1025
    # http://54.201.47.219:8080/api/v1/test1_results/
    # http://54.201.47.219:8080/api/v1/test1_results/1025
    # http://54.201.47.219:8080/api/v1/test1_weights/

    pprint(get_students())
    
    pprint(get_student(1024))
    update_student(1024, {'rank': 42})
    pprint(get_student(1024))

    add_student({"id": 1234, "fullname": "AAAA",
                 "email": "x@y.z", "github": "", "rank": 0})
    pprint(get_student(1234))

    reset()
    pprint(get_students())

    
#------------------------------------------------------------------------------
def update_students_results():
    '''
    Calculate student results and put them into the
    student dictionary under the key "rank".
    Total rank is calculated as a sum of completed hw tasks +
    sum of completed Test1 tasks weighted proportional to its weights.
    For example, student with id=1025 has
    total rank = 1*32 + (1*1 + 1*1 + 1*1 + ... 1*15) = 68)
    :return: None
    '''
    students = get_students()
    home_works = get_hw_results()
    test1_results = get_test1_results()
    test1_weights = get_test1_weights()
    
    for student in students:
        student_id = student['id']
        hw_rank = sum(home_works[student_id])
        test1_result = test1_results[student_id]
        test1_rank = sum([test1_result[i]*test1_weights[i] for i in range(NUM_OF_TESTS)])
        total_rank = hw_rank + test1_rank
        update_student(student_id, {'rank': total_rank})


#------------------------------------------------------------------------------
def print_students_info(sort_by_key="fullname"):
    '''
    Prints students info sorted according to the passed key in dictionary).
    By default, sort by students names.
    Student info should be presented as a card that includes
    the following information:
        - id,
        - name,
        - email,
        - github account (only name, not URL path)
        - rank
    Example (format is not strictly required):
        -----------------------------------------
        : ID:                               1025:
        :.......................................:
        : Full name:                Юношев Павел:
        : Email:          p.n.yunoshev@gmail.com:
        : Github:                               :
        : Rank:                               42:
        -----------------------------------------
    :return: None
    '''
    students = get_students()

    students_right_order = sorted(students, key=lambda k: k[sort_by_key])
    
    def print_student(student):

        message = []
        for field in student.keys():
            line = ("%s: %s" % (field, student[field]))
            message.append(line)
            
        table_width = max([len(w) for w in message])
        cover = " +" + "-"*table_width + "-+"
        print(cover)
        for k, v in student.items():
            if k == "github" and v:
                v = v.split("/")[3]
            elif k == "github":
                v = "¯\_(o.O)_/¯"
                
            xtr_spaces = table_width - len(k) - len(str(v))
            print("| %s:%s%s |" % (k, " "*xtr_spaces, v))
        print(cover)
        print()
    
    for student in students_right_order:
        print_student(student)


#------------------------------------------------------------------------------
if __name__ == "__main__":
    # demo()
    # print("hello, Im Main")
    update_students_results()
    print_students_info()
    reset()

