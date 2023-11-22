import unittest

def area(a, b):
    '''Принимает числа a и b, возвращает ab - площадь прямоугольника
    При вызове функции print(area(1, 2)) выведет 2 - площадь прямоугольника со сторонами a=1 и b=2'''
    if (a>0) and (b>0):
        return a * b
    else:
        return "error"
    
def perimeter(a, b):
    '''Принимает числа a и b, возвращает 2a + 2b - периметр прямоугольника'''
    '''При вызове функции print(perimeter(1, 2)) выведет 6 - периметр прямоугольника со сторонами a=1 и b=2'''
    if (a>0) and (b>0):
        return 2*(a + b)
    else:
        return "error"


