def area(a, b):
     '''
     Принимает два числа, которые являются сторонами прямоугольника: a, b
     Возвращает площадь прямоугольника, перемножая число a на число b: a * b
     '''
     if (a < 0 or b < 0):
          raise ValueError("Incorrect value")
     return a * b
def perimeter(a, b):
     '''
     Принимает два числа, которые являются сторонами прямоугольника: a, b
     Возвращает периметр прямоугольника, вычисляя его по формуле: P = 2 * (a + b)
     '''
     if (a < 0 or b < 0):
          raise ValueError("Incorrect value")
     return 2 * (a + b)
