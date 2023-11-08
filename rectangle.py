def area(a, b):
    """Принимает две смежные стороны и выводит площадь прямоугольника"""
    if a >= 0 and b >= 0:
        return a * b
    else:
        return 0

def perimeter(a, b):
    """Принимает две смежные стороны и выводит периметр прямоугольника"""
    if a >= 0 and b >= 0:
        return (a + b) * 2
    else:
        return 0
