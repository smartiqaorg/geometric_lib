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

| Name of File | Function  | Sequencing     | Consisting | Facted Result | Expected Result | Verdict   |
|--------------|-----------|----------------|------------|---------------|-----------------|-----------|
| rectangle.py | area      | Input data     | 0, 244     | 0             | 0               | correct   |
| rectangle.py | area      | Input data     | 2355, -6   | -14130        | ERROR           | incorrect |
| rectangle.py | area      | Input data     | 31, 23     | 713           | 713             | correct   |
| rectangle.py | perimeter | Input data     | 13, 244    | 514           | 514             | correct   |
| rectangle.py | perimeter | Input data     | 31, 23     | 108           | 108             | correct   |
| rectangle.py | perimeter | Input data     | 2355, 6    | 4722          | 4722            | correct   |
| square.py    | area      | Input data     | 13         | 169           | 169             | correct   |
| square.py    | area      | Input data     | 100.5      | 10100.25      | 10100.25        | correct   |
| square.py    | area      | Input data     | 31         | 961           | 961             | correct   |
| square.py    | perimeter | Input data     | -13        | -52           | ERROR           | incorrect |
| square.py    | perimeter | Input data     | 31         | 124           | 124             | correct   |
| square.py    | perimeter | Input data     | 100        | 400           | 400             | correct   |
| triangle.py  | area      | Input data     | -100, -50  | 2500          | ERROR           | incorrect |
| triangle.py  | area      | Input data     | 3, 14      | 21            | 21              | correct   |
| triangle.py  | area      | Input data     | 45, 5      | 112.5         | 112.5           | correct   |
| triangle.py  | perimeter | Input data     | 100, 1, 1  | 102           | ERROR           | incorrect |
| triangle.py  | perimeter | Input data     | 23, 24, 14 | 61            | 61              | correct   |
| triangle.py  | perimeter | Input data     | 45, 45, 4  | 94            | 94              | correct   |
| circle.py    | area      | Input data     | 50         | 7853.981      | 7853.981        | correct   |
| circle.py    | area      | Input data     | -2         | 12.566        | ERROR           | incorrect |
| circle.py    | area      | Input data     | 44         | 6082.123      | 6082.123        | correct   |
| circle.py    | perimeter | Input data     | 50         | 314.159       | 314.159         | correct   |
| circle.py    | perimeter | Input data     | 2          | 12.566        | 12.566          | correct   |
| circle.py    | perimeter | Input data     | 4          | 25.132        | 25.132          | correct   |


