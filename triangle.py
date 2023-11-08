def area(a, h):
    """Принимает длину высоты и противоположную сторону и выводит площадь"""
    if a >= 0 and h >= 0:
        return a * h / 2
    else:
        return 0

def perimeter(a, b, c):
    """Принимает три стороны треугольника и выводит периметр"""
    if a + b > c and a + c > b and b + c > a:
        return a + b + c
    else:
        return 0