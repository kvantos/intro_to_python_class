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
    MAX_STOMACH_FILL = 90  # in percent
    
    def __init__(self, stomach_total_volume=100):
        self.stomach_total_volume = stomach_total_volume
        self.stomach_current_volume = 0  # in percent

    def eat(self, human_weight):
        # human weight in percent
        human_weight_p = (100*human_weight)/self.stomach_total_volume
        
        if human_weight_p > Godzilla.MAX_STOMACH_FILL:
            print("Hey, its too much even for me!")
            
        elif self.stomach_current_volume >= Godzilla.MAX_STOMACH_FILL:
            print("I'm full and can not eat more.")
        
        elif self.stomach_current_volume + human_weight_p <= Godzilla.MAX_STOMACH_FILL:
            print("Delicious, thanks!")
            self.stomach_current_volume += human_weight_p

        else:
            left_space = (Godzilla.MAX_STOMACH_FILL - self.stomach_current_volume)*self.stomach_total_volume/100
            print("human person with weight %i is too much" % human_weight)
            print("Cant eat such a big human. However, I still able to absorb")
            print("human with weight around %i" % left_space)
        
        
class Circle:
    """
    35. Создать два класса: Окружность и Точка. Создать
    в классе окружности метод, который принимает в качестве
    параметра точку и проверяет находится ли данная
    точка внутри окружности.
    """
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def check_dot(dot):
        pass


class TheDot:
    def __init__(self, x, y):
        self.x = x
        self.y = y


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
            
        


