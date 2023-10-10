import math

def area(r):
    '''
    Возвращает произведение квадрата r на pi.
    :param r: десятичное число.
    :return: число, состоящее из произведения r на r на Pi.
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Возвращает удвоенное произведение двух чисел.
    :param r: десятичное число.
    :return: число, состоящее из произведение 2 на число pi на r.
    '''
    return 2 * math.pi * r