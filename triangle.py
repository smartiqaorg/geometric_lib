def is_triangle(a, b, c):
    """
    Проверяет, являются ли три числа сторонами треугольника.
    """
    return a + b > c and a + c > b and b + c > a

def area(a, h):
     '''
     Принимает два числа, которое являются высотой и стороной треугольника: a, h
     Возвращает площадь треугольника, вычисляя её по формуле: 0.5 * a * h
     '''
     if (a < 0 or h < 0):
          raise ValueError("Invalid value")
     return a * h / 2
def perimeter(a, b, c):
     '''
     Принимает 3 числа, которые являются сторонами треугольника: a, b, c
     Возвращает периметр треугольника, вычисляя его по формуле: P = a + b + c
     '''
     if (a < 0 or b < 0 or c < 0):
          raise ValueError("Invalid value")
     if (not is_triangle(a, b, c)):
          raise ValueError("Invalid value")
     return a + b + c
