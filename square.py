def area(a):
    if (a <= 0) or isinstance(a,str) or isinstance(str,a):
        return "Invalid input"
    '''
    На вход поступает число:
            a (int): длина стороны квадрата
    Функция возвращает квадрат числа a.
    '''
    return a * a


def perimeter(a):
    if (a <= 0) or isinstance(a,str) or isinstance(str,a):
        return "Invalid input"
    '''
    На вход поступает число:
            a (int): длина стороны квадрата
    Функция возвращает число a умноженное на 4.
    '''
    return 4 * a

