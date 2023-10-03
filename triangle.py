def area(a, h):
    '''
    возвращает площадь треугольника с длиной одной из сторон a, и длины высоты, которая к ней проведена, h.

        Парметры:
            a - длина одной из сторон (число)
            h - длина высоты, которая проведена к указанной стороне. (число)

        Возвращаемое значение:
            Полупроизведение высоты на эту сторону, то есть площадь треугольника.
    '''
    return a * h / 2 

def perimeter(a, b, c):
    '''
    Возвращает периметр треугольника со сторонами a, b, c (числа)

        Входные данные:
            a - длина первой стороны (число)
            b - длина второй стороны (число)
            c - длина третьей стороны (число)

        Возвращаемое значение (число): сумма a, b, c.
    '''
    return a + b + c 