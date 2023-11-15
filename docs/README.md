# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a

***Лабораторная работа №2***
### Общее описание решения:
- Вычисление периметра и площади заданных фигур: круга, треугольника, прямоугольника и квадрата. 

### Описание каждой функции: 
-circle.py:
#### Возвращает площадь круга с радиусом r:
def area(r):
    return a * a
_Параметры_ (радиус): 10
_Возвращаемое значение:_
 ~78,54

#### Возвращает периметр круга с радиусом r
def perimeter(r):
    return 2 * math.pi * r
_Параметры_ (радиус): 10
_Возвращаемое значение:_ ~62,83

-rectangle.py:
#### Возвращает площадь прямоугольника со стороной a и стороной b
def area(a, b):
    return a * b
_Параметры_ (ширина, длина): 10, 5
_Возвращаемое значение:_ 50

#### Возвращает периметр прямоугольника со стороной a и стороной b
def perimeter(a, b):
    return 2*a + 2*b
_Параметры_ (ширина, длина): 10, 5
_Возвращаемое значение:_ 30

-square.py:
#### Возвращает площадь квадрата со стороной a
def area(a):
    return a * a
_Параметры_ (сторона): 5
_Возвращаемое значение:_ 25

#### Возвращает периметр квадрата со стороной a
def perimeter(a):
    return 4 * a
_Параметры_ (сторона квадрата): 5
_Возвращаемое значение:_ 20

-triangle.py
#### Возвращает площадь треугольника со стороной a и высотой h
def area(a, h):
    return a * h / 2
_Параметры_ (сторона, высота): 10, 4
_Возвращаемое значение:_ 20

#### Возвращает периметр треугольника со сторонами a, b, c
def perimeter(a, b, c):
    return a + b + c
Параметры (сторона, сторона, сторона): 6, 4, 8
Возвращаемое значение: 18

## История изменения проекта с хешами комитов (кроме последней записи):
+ 7b61707de8d0b4c628770e71e00451d86d73bbe5 (HEAD -> new_features_000002) docs: added documentation for square.py
+ 5a1d9d0924ead3c135c6f3e84cbf79f3b3093865 docs: added documentation for rectangle.py
+ 571e280f967ce428219fa31762574bf62b9b87ab docs: added documentation for triangle.py
+ ce04e014a0a4adecf578660a466270f004f4e3be docs: added documentation for circle.py
+ 4973d225376eccaaa2b537be9fc59ef57a46bc50 docs: added documentation for circle.py
