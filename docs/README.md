# Math formulas
В каждом из 4 файлов python содержатся функции, считающие площадь и периметр 4 фигур:
- круг
- прямоугольник
- квадрат
- треугольник

## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: S = ah / 2

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle: P = a + b + c

## Functions 
- ### circle.py
  - ##### area(r)
  
    Принимает число r - радиус круга, возвращает число возведенное в квадрат и домноженное на пи - площадь круга
    ```
    print(area(5))
    -> 78.53981633974483
    ```
  - ##### perimeter(r)
    
    Принимает число r - радиус круга,возвращает число домноженное на два и на пи - периметр круга
    ```
    print(perimeter(5))
    -> 31.41592653589793
    ```
- ### rectangle.py
  - ##### area(a,b)
    
    Принимает два числа a и b - стороны прямоугольника,возвращает произведение двух чисел - площадь прямоугольника
    ```
    print(area(5,6))
    -> 30
    ```
  - ##### perimeter(a,b)
    ```
    print(perimeter(5,6))
    -> 22
    ```
    
    Принимает два числа a и b - стороны прямоугольника,возращает сумму двух чисел домноженную на два
- ### triangle.py
  - ##### area(a,h)
    Принимает два числа a - сторона треугольника и h - высота, опущенная к стороне треугольника,
    возвращает произведение двух чисел деленное на два - площадь треугольника
    ```
    print(area(5,6))
    -> 15
    ```
  - ##### perimeter(a,b,c)
    Принимает три числа a, b, c - стороны трегольника,
    возвращает сумму трех чисел - периметр треугольника
    ```
    print(perimeter(5,7,8)
    -> 20
    ```
- ### square.py
  - ##### area(a)
    Принимает число a - сторону квадрата,
    возвращает квадрат числа - площадь квадрата
    ```
    print(area(5))
    -> 25
    ```
  - ##### perimeter(a)
    Принимает число a - сторону квадрата,
    возвращает число умноженное на четыре - периметр квадрата
    ```
    print(perimeter(5))
    -> 20
    ```
## История изменения проекта с хешами коммитов
* **e4f08ec** (HEAD -> documentation_408912) updated rectangle.py
* **1dd3702** added comments to functions in all .py files
* **def3a90** (origin/main, origin/HEAD, main) triangle.py created and bug fixed
* **09bb1fa** new file rectangle.py created
* **d078c8d** L-03: Docs added
* **8ba9aeb** L-03: Circle and square added

## Unit Tests
Для проверки корректности работы функций были созданы unit тесты. В папке unit_tests были созданы файлы python с соответствующими для каждой фигуры тестами.

В каждом файле содержатся тесты 4 типов:
- тест при неправильном типе переданного аргумента
- тест при недопустимом значении переданного аогумента
- тест при нулевом значении переданного аргумента
- тест на соответствие результату значения, посчитанному вручную

- ### circle_test.py
  Unit test success: 2/8 = 0.25 
  - test_area &#10003; 
  - test_perimeter &#10003;
- ### rectangle_test.py
  Unit test success: 2/8 = 0.25
  - test_area &#10003;
  - test_perimeter &#10003;
- ### square_test.py
  Unit test success: 1/8 = 0.125
  - test_area &#10003;
- ### triangle_test.py
  Unit test success: 2/8 = 0.25
  - test_area &#10003;
  - test_perimeter &#10003;

