# <span style="color:darkred">Документация</span>

## <span style="color:chocolate">Circle</span>

### <span style="color:goldenrod">Общее описание решения</span>

Файл содержит функции, необходимые для вычисления периметра и площади круга

### <span style="color:goldenrod">Функции</span>

**AREA**

Функция принимает на вход радиус круга (r) и возвращает площадь

```python
def area(r):
     return math.pi * r * r
```

Пример вызова:

```python
import math
r = 5
A_circle = area(r)
print("Площадь: ", A_circle)   #78.5375
```

**PERIMETER**

Функнкция принимает на вход радиус круга (r) и возвращает периметр

```python
def perimeter(r):
    return 2 * math.pi * r
```

Пример вызова:

```python
r = 5
P_circle = perimeter(r)
print("Периметр: ", P_circle)   #31.415
```

## <span style="color:chocolate">Square</span>

### <span style="color:goldenrod">Общее описание решения</span>

Файл содержит функции, необходимые для вычисления периметра и площади квадрата

### <span style="color:goldenrod">Функции</span>

**AREA**

Функция принимает на вход сторону квадрата (a) и возвращает площадь

```python
def area(a):
    return a * a
```

Пример вызова:

```python
a = 5
A_square = area(a)
print("Площадь: ", A_square)   #25
```

**PERIMETER**

Функнкция принимает на вход сторону квадрата (a) и возвращает периметр

```python
def perimeter(a):
    return 4 * a
```

Пример вызова:

```python
a = 5
P_square = perimeter(a)
print("Периметр: ", P_square)   #20
```

## <span style="color:chocolate">Triangle</span>

### <span style="color:goldenrod">Общее описание решения</span>

Файл содержит функции, необходимые для вычисления периметра и площади треугольника

### <span style="color:goldenrod">Функции</span>

**AREA**

Функция принимает на вход основание (a) и высоту (h) треугольника и возвращает площадь

```python
def area(a, h):
    return a * h / 2
```

Пример вызова:

```python
a = 5
h = 10
A_triangle = area(a, h)
print("Площадь: ", A_triangle)   #25
```

**PERIMETER**

Функция принимает на вход длины сторон треугольника (a, b, c) и возвращает площадь

```python
def perimeter(a, b, c):
     return a + b + c
```

Пример вызова:

```python
a = 5
b = 6
c = 4
P_triangle = perimeter(a, b, c)
print("Периметр: ", P_triangle)   #15
```
## <span style="color:chocolate">Rectangle</span>

### <span style="color:goldenrod">Общее описание решения</span>

Файл содержит функции, необходимые для вычисления периметра и площади прямоугольника

### <span style="color:goldenrod">Функции</span>

**AREA**

Функция принимает на вход длину (a) и ширину (b) прямоугольника и возвращает площадь

```python
def area(a, b):
    return a * b
```

Пример вызова:

```python
a = 5
b = 10
A_rectangle = area(a, b)
print("Площадь: ", A_rectangle)   #50
 ```

**PERIMETER**

Функция принимает на вход длину (a) и ширину (b) прямоугольника и возвращает площадь

```python
def perimeter(a, b):
    return (a + b)*2
```

Пример вызова:

```python
a = 5
b = 10
P_rectangle = perimeter(a, b)
print("Периметр: ", P_rectangle)   #30
```
## <span style="color:chocolate">История изменения проекта</span>

| Хэш коммита        | Автор      | Дата                                                                | Комментарий                            |
|--------------------|------------|---------------------------------------------------------------------|----------------------------------------|
|889e7e1ac118f3372400db451b65ef14615559a2|Ermolaeva Daria <darerm1@yandex.ru>|Wed Oct 11 10:37:28 2023 +0300|docs: add documentation to triangle.py|
|4aaf113bcb2077c446139b0ce6b5f1efb1ff6cda|Ermolaeva Daria <darerm1@yandex.ru>|Wed Oct 11 10:36:29 2023 +0300|docs: add documentation to square.py|
|1dbe2ee6060d925624336c44a05f9d09ab397ce0|Ermolaeva Daria <darerm1@yandex.ru>|Wed Oct 11 10:35:32 2023 +0300|docs: add documentation to rectangle.py|
|f74016124b257cf67acdd084111f55776b7061ed|Ermolaeva Daria <darerm1@yandex.ru>|Wed Oct 11 10:29:09 2023 +0300|docs: add documentation to circle.py|
