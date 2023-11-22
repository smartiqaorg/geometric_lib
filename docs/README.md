# Geometric Lib
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://camo.githubusercontent.com/fc8cea0dacea7dd19a09aacf06109ccfa5ed931fa471c0beffb5acacbaa39c33/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f505954484f4e2d626c61636b3f7374796c653d666f722d7468652d6261646765266c6f676f3d707974686f6e266c6f676f436f6c6f723d676f6c64">
  <source media="(prefers-color-scheme: light)" srcset="https://camo.githubusercontent.com/fc8cea0dacea7dd19a09aacf06109ccfa5ed931fa471c0beffb5acacbaa39c33/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f505954484f4e2d626c61636b3f7374796c653d666f722d7468652d6261646765266c6f676f3d707974686f6e266c6f676f436f6c6f723d676f6c64">
  <img alt="Shows an illustrated sun in light mode and a moon with stars in dark mode." src="https://camo.githubusercontent.com/fc8cea0dacea7dd19a09aacf06109ccfa5ed931fa471c0beffb5acacbaa39c33/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f505954484f4e2d626c61636b3f7374796c653d666f722d7468652d6261646765266c6f676f3d707974686f6e266c6f676f436f6c6f723d676f6c64">
</picture>

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
- Square: P = 4a
- Triangle: P = a + b + c

## Functions 
- ### circle.py
  - ##### area(r)

    Принимает число r - радиус круга, возвращает число возведенное в квадрат и домноженное на пи - площадь круга
    ```
    print(area(6))
    -> 113.04
    ```
  - ##### perimeter(r)
    
    Принимает число r - радиус круга,возвращает число домноженное на два и на пи - периметр круга
    ```
    print(perimeter(6))
    -> 37.68
    ```
- ### rectangle.py
  - ##### area(a,b)
    
    Принимает два числа a и b - стороны прямоугольника,возвращает произведение двух чисел - площадь прямоугольника
    ```
    print(area(4,5))
    -> 20
    ```
  - ##### perimeter(a,b)
    ```
    print(perimeter(4,5))
    -> 18
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
    print(perimeter(6,7,8)
    -> 21
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
### Хеш коммитов:
| хеш коммита | автор коммита               | комментарий                   |
|-------------|-----------------------------|-------------------------------|
| 94b52e3     | gront <408507@edu.itmo.ru>  | comment to the cod            |
| 106df63     | gront <408507@edu.itmo.ru>  | the bug has been fixed        |
| 95efe91     | gront <408507@edu.itmo.ru>  | Add new file                  |
| d078c8d     | smartiqa <info@smartiqa.ru> | L-03: Docs added              |
| 8ba9aeb     | smartiqa <info@smartiqa.ru> | L-03: Circle and square added |

# Unit-tests
## всего сделано 29 unit-тестов 
 **rectangle.py**

***результат:***

___6 тестов: 6 тестов успешно___

#### успешно:

- `area()`
```
cin: 5 0
cout: 0
```
```
cin: 5 5 
cout: 25
```
```
cin: 5.5 5.42
cout: 29.81
```
- `perimeter()`
```
cin: 0 0
cout: 0
```
```
cin: 5 4
cout: 18
```
```
cin: 5.9 2.23
cout: 16.26
```
---
 **circle.py**
 
***результат***

___6 тестов: 4 теста успешно, 2 теста с ошибкой___

### успешно:
- `area()`
```
cin: 0
cout: 0
```
```
cin: 6
cout: 113.09733552923255
```
- `perimeter()`
```
cin: 0
cout: 0
``` 
```
cin: 5 
cout: 31.41592653589793
```
### c ошибкой:
- `area()`
```
cin: -4
cout: 50.26548245743669 (ожидалось -1, ошибка)
```
- `perimeter()`
```
cin: -5
cout: -31.41592653589793 (ожидалось -1, ошибка)
```
---
**square.py**

***результат***

___8 тестов: 6 тестов успешно, 2 теста с ошибкой___

### успешно:
- `area()`
```
cin: 0
cout: 0
```
```
cin: 5
cout: 25
```
```
cin: 5.25
cout: 27.5625
```

- `perimeter()`
```
cin: 0
cout: 0
``` 
```
cin: 5 
cout: 20
```
```
cin: 5.9
cout: 23.6
```
### c ошибкой:
- `area()`
```
cin: -3
cout: 9 (ожидалось -1, ошибка)
```
- `perimeter()`
```
cin: -3
cout: -12 (ожидалось -1, ошибка)
```
---

**triangle.py**

***результат***

___9 тестов: 6 тестов успешно, 3 теста с ошибкой___

### успешно:
- `area()`
```
cin: 0 0 
cout: 0
```
```
cin: 5 3
cout: 7.5
```
```
cin: 5.1 4.76
cout: 12.137999999999998
```
- `perimeter()`
```
cin: 0 0 0
cout: 0
``` 
```
cin: 5 7 10
cout: 22
```
```
cin: 5.45 1.21 8.35
cout: 15.01
```
### c ошибкой:
- `area()`
```
cin: 5 -1
cout: -2.5 (ожидалось -1, ошибка)
```
```
cin: -5 1
cout: -2.5 (ожидалоь -1, ошибка)
```
- `perimeter()`
```
cin: -9 10 4
cout: 5 (ожидалось -1, ошибка)
```
---
