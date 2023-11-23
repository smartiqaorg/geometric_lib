# Math formulas
Library for calculating the area and perimeter of geometric shapes. Functions available for triangle, circle, rectangle and square.

## Area - examples of using
- Circle: S = πR²
```
radius = 5
area = square.area(radius)
```
- Rectangle: S = ab
```
a = 5
b = 10
area = rectangle.area(a, b)
```
- Square: S = a²
```
a = 5
area = square.area(a)
```
- Triangle: S = a * h / 2 
```
a = 5
h = 15
area = traingle.area(a, h)
```

## Perimeter
- Circle: P = 2πR
```
r = 5
perimeter = circle.perimeter(r)
```
- Rectangle: P = 2a + 2b
```
a = 5
b = 13
perimeter = rectangle.perimeter(a, b)
```
- Square: P = 4a
```
a = 5
perimeter = square.perimeter(a)
```
- Triangle: P = a + b + c
```
a = 3
b = 4
c = 5
perimeter = traingle.perimeter(a, b, c)
```
## History of project

That table not include of last commits with information about added documentation.

| Commit Hash | Branch                       | Author            | Date                           | Description                                     |
|-------------|------------------------------|-------------------|--------------------------------|-------------------------------------------------|
| 83781e20    | new_features_412943, main    | alinazh           | Tue Sep 19 00:51:47 2023 +0300 | Отрекдактирован файл rectangle.py. Исправлено вычисление периметра. |
| 4c013c19    | new_features_412943, main    | alinazh           | Tue Sep 19 00:46:56 2023 +0300 | Добавлен файл rectangle.py                     |
| d078c8d9    | origin/main, origin/HEAD     | smartiqa          | Thu Mar 4 14:55:29 2021 +0300  | L-03: Docs added                                |
| 8ba9aeb3    | origin/main, origin/HEAD     | smartiqa          | Thu Mar 4 14:54:08 2021 +0300  | L-03: Circle and square added                  |

## Testing by UnitTest

Launched 24 tests, 5 of them were incorrect, 19 tests were correct.
