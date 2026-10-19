def area(a, b):
    
    '''
    Возвращает значение площади прямоугольника с заданными сторонами

    Параметры:
        a (float): первая сторона
        b (float): вторая сторона

    Возвращаемое значение:
        rectangle_area (float): площадь прямоугольника со сторонами a и b 
    '''

    rectangle_area = a * b
    return rectangle_area

def perimeter(a, b):

    '''
    Возвращает значение периметра прямоугольника с заданными сторонами

    Параметры:
        a (float): первая сторона
        b (float): вторая сторона

    Возвращаемое значение:
        rectangle_perimeter (float): периметр прямоугольника со сторонами a и b 
    '''

    rectangle_perimeter = 2 * (a + b)
    return rectangle_perimeter