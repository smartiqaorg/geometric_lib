def area(a, h):

    '''
    Возвращает значение площади треугольника с заданной стороной и с заданной высотой

    Параметры:
        a (float): сторона треугольника
        h (float): высота треугольника

    Возвращаемое значение:
        triangle_area (float): высота треугольника со стороной a и высотой h 
    '''

    triangle_area = a * h / 2
    return triangle_area

def perimeter(a, b, c):
    
    '''
    Возвращает значение периметра треугольника с заданными сторонами

    Параметры:
        a (float): первая сторона
        b (float): вторая сторона
        с (float): третья сторона

    Возвращаемое значение:
        tria ngle_perimeter (float): периметр треугольник со сторонами a, b и c 
    '''

    triangle_perimeter = a + b + c
    return triangle_perimeter

