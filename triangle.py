def area(a, h):
    '''Принимает значения a и h, соответствующие стороне и высоте треугольника. Возвращает площадь треугольника'''
    if a > 0 and h > 0:
        return a * h / 2
    else:
        return 0

def perimeter(a, b, c):
    '''Принимает значения a, b, c, соответсвующие сторонам треугольника. Возвращает периметр треугольника'''
    if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a:
        return a + b + c
    else:
        return 0

