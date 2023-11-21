import math

def area(r):
    '''
    Принимает число r, значение r - радиус круга

      Параметры:
          r (int) или (float)

      Возвращаемое значение:
        Площадь круга (int) или (float)
     '''

    return math.pi * r * r


def perimeter(r):
    '''
        Принимает число r, значение r - радиус круга

          Параметры:
              r (int) или (float)

          Возвращаемое значение:
            Периметр круга (int) или (float)
         '''
    return 2 * math.pi * r
