# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: S = a*h/2

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle: P = a + b + c

# Functions
## Circle
### Area
- import math Подключаем библиотеку с математическими функциями

  Функция для нахождения площади круга с заданным радиусом

  def area(r):
    
     Принимает r - радиус, возвращает площадь круга с заданным радиусом
    
     return math.pi*r *r

### Perimeter
- import math Подключаем библиотеку с математическими функциями

  Функция для нахождения длины окружности с заданным радиусом

  def perimeter(r):
    
     Принимает r - радиус, возвращает длину окружности с заданным радиусом
    
     return 2*math.pi*r

## Rectangle
### Area
- Функция для нахождения площади прямоугольника по заданным параметрам a и b

  def area(a, b):
    
    Возвращает произведение двух чисел

        Параметры:

            a(int): длина прямоугольника
            b(int): ширина прямоугольника

        Вовзвращаемое значение:
        
            area(int): произведение чисел a и b
    
    return a * b
### Perimeter
- Функция для нахождения периметра прямоугольника по заданным парметрам a и b

  def perimeter(a, b):
    
    Возвращает удвоенную сумму параметров a и b

        Параметры:

            a(int): длина прямоугольника
            b(int): ширина прямоугольника

        Возвращаемое значение:

            perimeter(int): удвоенная сумма параметров a и b
    
    return 2*a + 2*b

## Square
### Area
- Функция для нахождения площади квадрата по заданному параметру

  def area(a):
    
    Принимает параметр a, возвращает произведение параметра a на самого себя
    
    return a * a
### Perimeter
- Функция для нахождения периметра квадрата по заданному параметру

def perimeter(a):
    
    Принимает параметр a, возвращает произведение параметра a и 4
    
    return 4 * a

## Triangle
### Area
- Функция для нахождения площади треугольника по заданнымы параметрам

  def area(a, h):
    
    Возвращает площадь треугольника по формуле s=a*h/2

        Параметры:
            a(int): длина основания треугольника
            h(int): длина высоты треугольника


        Возвращаемое значение:
            area(int): половина произведения a и h
    
    return a * h / 2
### Perimeter
- Функция для нахождения периметра треугольника по заданным параметрам

  def perimeter(a, b, c):
    
    Возвращает сумму трех параметров a, b и c

        Параметры:
            a(int): длина первой стороны треугольника
            b(int): длина второй стороны треугольника
            c(int): длина третьей стороны треугольника


        Возвращаемое значение:
            perimeter(int): сумма a, b и c
    
    return a + b + c
# Unittests
- 18/26 unitetsts have been completed
# Commits
- kimurtim19 | Thu Sep 21 22:38:50 2023 +0300 | 885b5e12421b4ae483e223d1517e047930f9e7e3 | corrected spelling errors
- kimurtim19 | Thu Sep 21 22:36:37 2023 +0300 | e581c81d4f1995cda14f58246a05eadd33a58a1d | documentation for triangle.py
- kimurtim19 | Thu Sep 21 22:16:20 2023 +0300 | ac7d98ef0e73390f935c0d09e36fd97e2965d4c5 | documentation for square.py
- kimurtim19 | Thu Sep 21 22:09:34 2023 +0300 | 71ec08efc8f7a830bf3bfbadaf9709d0c246b5d5 | documentation for rectangle.py
- kimurtim19 | Thu Sep 21 21:54:12 2023 +0300 | da40b302f5d91b20e10fa641baeaffc1f522ed09 | documentation for circle.py
- kimurtim19 | Tue Nov 14 16:12:32 2023 +0300 | 88cce5b2461f70867c74495a8869158a44d13fd4 | 4 unittests have been added
