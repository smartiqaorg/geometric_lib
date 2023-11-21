# Math formulas

Данный проект содержит файлы .py, в каждом из которых объявлены функции для подсчёта площадей и периметров четырёх геометрических фигур:

- круг
- прямоугльник
- треугольник
- квадрат

## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a

## Functions
- ### circle.py
  - ##### area(r) 
    Принимает число r - радиус окружности, возвращает площадь круга с радиусом r (произведение числа Пи на квадрат радиуса r):
    ```
    print(area(5))
    -> 78.53981633974483
    ``` 
  - ##### perimeter(r)
    Принимает число r - радиус окружности, возвращает длину окружности с радиусом r (удвоенное произведение числа Пи на радиус r):
    ```
    print(perimeter(5))
    -> 31.41592653589793
    ``` 
    
- ### rectangle.py
  - ##### area(a, b)
    Принимает 2 числа: a и b, - стороны прямоугольника. Возвращает площадь прямоугольника со сторонами a и b (произведение чисел a и b):
    ```
    print(area(4, 5))
    -> 20
    ``` 
  - ##### perimeter(a, b)
    Принимает 2 числа: a и b, - стороны прямоугольника. Возвращает периметр прямоугольника со сторонами a и b (удвоенную сумму чисел a и b):
    ```
    print(perimeter(4, 5))
    -> 18
    ``` 

- ### square.py
  - ##### area(a)
    Принимает число a - сторону квадрата, возвращает площадь квадрата со стороной a (квадрат числа a):
    ```
    print(area(5))
    -> 25
    ``` 
  - ##### perimeter(a)
    Принимает число a - сторону квадрата, возвращает периметр квадрата со стороной a (произведение числа a на 4):
    ```
    print(perimeter(5))
    -> 20
    ``` 

- ### triangle.py
  - ##### area(a, h)
    Принимает 2 числа: a и h, - основание треугольника и высота к этому основанию соответственно. Возвращает площадь треугольника с основанием a и высотой к этому основанию h (половина произведения чисел a и h):
    ```
    print(area(5, 4))
    -> 10
    ``` 
  - ##### perimeter(a, b, c)
    Принимает 3 числа: a, b и c, - стороны треугольника. Возвращает периметр треугольника со сторонами (половина произведения чисел a и h):
    ```
    print(perimeter(3, 4, 5))
    -> 12
    ``` 
    

## Unit tests
-  Тесты, которые проверяют корректность работы функций в файлах  circle.py, rectangle.py, square.py и triangle.py.

### CircleTestCase
```python
class CircleTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(5), 78.53981633974483) # successful test
        self.assertEqual(area(7), 315) # fail test
        self.assertEqual(area('string'), 'fail')  # fail test

    def test_perimeter(self):
        self.assertEqual(perimeter(5), 31.41592653589793) # successful test
        self.assertEqual(perimeter(10), 62)  # fail test
        self.assertEqual(perimeter('string'), 'fail')  # fail test
```

| Название теста | Ввод     | Ожидаемый Результат | Прошел тест или нет |
|----------------|----------|---------------------|---------------------|
| test_area      | 5        | 78.53981633974483   | <span style="color:green">true</span> |
| test_area      | 7        | 315                 | <span style="color:red">false</span> |
| test_area      | 'string' | fail                  | <span style="color:red">false</span> |
| test_perimeter | 5        | 31.41592653589793   | <span style="color:green">true</span> |
| test_perimeter | 10       | 62                  | <span style="color:red">false</span> |
| test_perimeter | 'string' | fail                | <span style="color:red">false</span> |

### RectangleTestCase 
```python
class RectangleTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(5, 2), 12) # successful test
        self.assertEqual(area(2, 3), 5) # fail test
        self.assertEqual(area('string', 4), 'fail')  # fail test

    def test_perimeter(self):
        self.assertEqual(perimeter(5, 2), 14) # successful test
        self.assertEqual(perimeter(10, 2), 62)  # fail test
        self.assertEqual(perimeter('string', 3), 'fail')  # fail test
```


| Название теста | Ввод          | Ожидаемый Результат | Прошел тест или нет |
|----------------|---------------|---------------------|---------------------|
| test_area      | (5, 2)        | 12                  | <span style="color:green">true</span> |
| test_area      | (2, 3)        | 5                   | <span style="color:red">false</span> |
| test_area      | ('string', 4) | fail                  | <span style="color:red">false</span> |
| test_perimeter | (5, 2)        | 14                  | <span style="color:green">true</span> |
| test_perimeter | (10, 2)       | 62                  | <span style="color:red">false</span> |
| test_perimeter | ('string', 8) | fail                | <span style="color:red">false</span> |


### SquareTestCase
```python
class SquareTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(5), 25) # successful test
        self.assertEqual(area(2), 6) # fail test
        self.assertEqual(area('string'), 'fail')  # fail test

    def test_perimeter(self):
        self.assertEqual(perimeter(5), 20) # successful test
        self.assertEqual(perimeter(10), 62)  # fail test
        self.assertEqual(perimeter('string'), 'fail')  # fail test
```

| Название теста | Ввод | Ожидаемый Результат | Прошел тест или нет |
|----------------|----|---------------------|---------------------|
| test_area      | 5  | 12                  | <span style="color:green">true</span> |
| test_area      | 10 | 5                   | <span style="color:red">false</span> |
| test_area      | 'string' | fail                | <span style="color:red">false</span> |
| test_perimeter | 5  | 20                  | <span style="color:green">true</span> |
| test_perimeter | 10 | 62                  | <span style="color:red">false</span> |
| test_perimeter | 'string' | fail                | <span style="color:red">false</span> |


### TriangleTestCase 
```python
class TriangleTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(5, 2), 12) # successful test
        self.assertEqual(area(2, 3), 5) # fail test
        self.assertEqual(area('string', 4), 'fail')  # fail test

    def test_perimeter(self):
        self.assertEqual(perimeter(5, 2, 3), 10) # successful test
        self.assertEqual(perimeter(10, 2, 1), 62)  # fail test
        self.assertEqual(perimeter('string', 3, 1), 'fail')  # fail test
```


| Название теста | Ввод             | Ожидаемый Результат | Прошел тест или нет |
|----------------|------------------|---------------------|---------------------|
| test_area      | (5, 2)           | 12                  | <span style="color:green">true</span> |
| test_area      | (2, 3)           | 5                   | <span style="color:red">false</span> |
| test_area      | ('string', 4)    | fail                   | <span style="color:red">false</span> |
| test_perimeter | (5, 2, 3)        | 10                  | <span style="color:green">true</span> |
| test_perimeter | (10, 2, 1)       | 62                  | <span style="color:red">false</span> |
| test_perimeter | ('string', 3, 1) | fail                | <span style="color:red">false</span> |


### Общие метрики
| Всего тестов | Выполнено                          | Провалено |
|--------------|------------------------------------|-----------|
| 24           | <span style="color:green">8</span> | <span style="color:red">16</span> |


## Project change history
* **261fd39** created new file and fixed bug in calculating perimetr rectangle
* **2c3a292** created rectangle.py
* **d078c8d** L-03: Docs added
* **8ba9aeb** L-03: Circle and square added
* **f1b0709** add Unittest


