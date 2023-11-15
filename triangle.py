def area (a,h):
    if (a <= 0 and h <= 0) or isinstance(a,str) or isinstance(str,a) or isinstance(h,str) or isinstance(str,h):
        return "Invalid input"
    '''
    На вход поступает два числа:
            a (int): длина стороны треугольника
            h (int): длина высоты треугольника
    Функция возвращает произведение  a и h деленное на 2.
    '''
    return a * h/2

def perimetr(a,b,c):
    if (a <= 0 and b <= 0 and c <= 0) or isinstance(a,str) or isinstance(b,str) or isinstance(str,a) or isinstance(str,b) or isinstance(c,str) or isinstance(str,c):
        return "Invalid input"
    '''
    На вход поступает три числа:
            a (int): длина стороны треугольника
            b (int): длина стороны треугольника
            c (int): длина стороны треугольника
    Функция возвращает сумму сторон треугольника.
    '''
    return a + b + c
