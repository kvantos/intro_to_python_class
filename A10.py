#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Godzilla:
    """
    34. Создать класс Годзила. У данного класса
    должен быть атрибут - объем желудка. Написать
    для данного класса метод поедания людей. В данную
    функцию должен передаваться объем съеденного и
    соответственно уменьшаться место в желудке. Когда
    Годзила заполнит желудок на 90%, метод должен
    выводить надпись, что Годзила наелся и больше не
    может поедать людей.
    """
    
    def __init__(self):
        self.stomach_volume = 0

    def eat(self, human_person):

        if human_person > 90:
            print("Hey, its too much even for me!")
            print("Averege humanperson should be around 20")
        else:
            self.stomach_volume += human_person
        
        if self.stomach_volume >= 90:
            print("I'm full and can not eat more.")
        

class Circle:
    """
    35. Создать два класса: Окружность и Точка. Создать
    в классе окружности метод, который принимает в качестве
    параметра точку и проверяет находится ли данная
    точка внутри окружности.
    """


class TheDot:

    def __init__(self, args):
        """
        
        """
        self.args = args
            

class Vehicle:
    """
    36. Создать класс Транспортное средство и его потомков
    - классы Поезд и Самолет. В родительском классе должно
    быть определено минимум 1 инициализатор, 3 атрибута и
    1 метод. В классах-потомках должны быть добавлены
    минимум по 1 новому методу и по 1 новому атрибуту.
    """

    def __init__(self, args):
        """
        
        """
        self.args = args
            
        


