# Math formulas

## Area

- Circle: S = πR²
- Rectangle: S = ab
- Triangle: S = $\frac{1}{2}$ ah
- Square: S = a²

## Perimeter

- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Triangle: P = a + b + c
- Square: P = 4a

# General desription

> With these programs you will be able to calculate the perimeter and area of various shapes

# Programs

## Circle

```python
import math
'''
Модуль math предоставляет обширный функционал для проведения вычислений
с вещественными числами (числами с плавающей точкой).
'''

def area(r):
    '''
    Принимает число, которое является радиусом круга: r
    Возвращает площадь круга, вычисляя её по формуле: π * r^2
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Принимает число, которое является радиусом круга: r
    Возвращает периметр круга, вычисляя его по формуле: P = 2 * π * r
    '''
    return 2 * math.pi * rdef
```

##### Example of a call

```python
r = 3
print(f"Area = {area(r)}; Perimetr = {perimetr(r)}")
```

```markdown
Output:
Area = 28.274333882308138; Perimeter = 18.84955592153876
```

## Rectangle

```python
def area(a, b):
     '''
     Принимает два числа, которые являются сторонами прямоугольника: a, b
     Возвращает площадь прямоугольника, перемножая число a на число b: a * b
     '''
     return a * b
def perimeter(a, b):
     '''
     Принимает два числа, которые являются сторонами прямоугольника: a, b
     Возвращает периметр прямоугольника, вычисляя его по формуле: P = 2 * (a + b)
     '''
     return 2 * (a + b)
```

##### Example of a call

```python
a = 4
b = 6
print(f"Area = {area(a, b)}; Perimetr = {perimetr(a, b)}")
```

```
Output:
Area = 24; Perimeter = 20
```


## Triangle

```python
def area(a, h):
     '''
     Принимает два числа, которое являются высотой и стороной треугольника: a, h
     Возвращает площадь треугольника, вычисляя её по формуле: 0.5 * a * h
     '''
     return a * h / 2
def perimeter(a, b, c):
     '''
     Принимает 3 числа, которые являются сторонами треугольника: a, b, c
     Возвращает периметр треугольника, вычисляя его по формуле: P = a + b + c
     '''
     return a + b + c
```

##### Example of a call

```python

a = 5
b = 3
c = 4
h = 2.4
print(f"Area = {area(a, h)}; Perimetr = {perimetr(a, b, c)}")
```

```
Output:
Area = 6; Perimeter = 12
```

## Square

```python
def area(a):
    '''
    Принимает число, которое является стороной квадрата: a
    Возвращает площадь квадрата, возводя число a в квадрат: a * a
    '''
    return a * a


def perimeter(a):
    '''
    Принимает число, которое является стороной квадрата: a
    Возвращает периметр квадрата, вычисляя его по формуле: P = 4 * a
    '''
    return 4 * a

```

##### Example of a call

```python
a = 5
print(f"Area = {area(a)}; Perimetr = {perimetr(a)}")
```

```
Output:
Area = 25; Perimeter = 20
```

# Commit history

```bash
commit d71b667f879923a334d9866f5daedb0b683f829a (HEAD -> main)
Author: CedoySch <cedoyscholnik@gmail.com>
Date:   Wed Sep 27 20:13:16 2023 +0300

    File Declaration #1

commit afe958db34f1914467a86d148d0fcfdf3f809e3c (origin/main, origin/HEAD)
Author: CedoySch <cedoyscholnik@gmail.com>
Date:   Thu Sep 14 21:23:37 2023 +0300

    rectangle.py changed

commit fcc8cf3db006e2be3f1433ce54d8db762da8c65f
Author: CedoySch <cedoyscholnik@gmail.com>
Date:   Thu Sep 14 21:21:44 2023 +0300

    triangle.py added

commit a495c62850dc7ceba69647267ac562cffd26b0b9
Author: CedoySch <cedoyscholnik@gmail.com>
Date:   Thu Sep 14 21:20:00 2023 +0300

    rectangle.py added

```
