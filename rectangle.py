def area ( a , b):
    if (a <= 0 and b <= 0) or isinstance(a,str) or isinstance(b,str) or isinstance(str,a) or isinstance(str,b):
        return "Invalid input"
    '''
    На вход поступает два числа:
            a (int): длина одной стороны
            b (int): длина другой стороны
    Функция возвращает значение равное произведению длины одной стороны на длину другой.
    '''
    return a * b
def perimeter (a,b):
    if (a <= 0 and b <= 0) or isinstance(a,str) or isinstance(b,str) or isinstance(str,a) or isinstance(str,b):
        return "Invalid input"
    '''
    На вход поступает два числа:
            a (int): длина одной стороны
            b (int): длина другой стороны
    Функция возвращает удвоенную сумму a и b.
    '''
    return (a + b) * 2

