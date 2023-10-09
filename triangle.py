def area(a, h):
    '''
        Возвращает площадь треугольника с основанием a и высотой h.

            Параметры:
                a(int): основание треугольника
                h(int): высота проведенная к стороне h

            Возвращаемое значение:
                 a * h/2(int): площадь  треугольника
        '''
    return a * h / 2 

def perimeter(a, b, c):
    '''
        Возвращает периметр треугольника со сторонами a b c.

            Параметры:
                a(int): первая сторона треугольника
                b(int): вторая сторона треугольника
                b(int): третья сторона треугольника

            Возвращаемое значение:
                a + b + с: периметр треугольника
    '''
    return a + b + c
