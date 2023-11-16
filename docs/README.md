# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a

# **Tests**

## 1. Цели и задачи тестирования
Основной целью тестирования является проверка соответствия поведения написанного кода ожидаемому поведению, требуется, чтобы код успешно проходил все тесты

## 2. Описание тестируемого продукта

Должна быть протестирована функциональность функций для вычисления площадей и периметров геометрических фигур, функций должны возвращать корректное значение.

## 3. Область тестирования

- ### Circle.py
    - area(r) - функцлия вычисления площадт круга радиуса **r**
    - perimeter(r) - функция вычисления длины окружности радиуса **r**

- ### Square.py
    - area(a) - функция вычисления площади квадрата с заданной стороной **а**
    - perimeter(a) - функция вычисления периметра квадрата с заданной стороной **a**

## 4. Стратегия тестирования
Тестирование исполнено с помощью Unit-тестов в виде функционального тестирования.

Будет проверено соответствуют ли возвращаемые функциями значения ожидаемым.
Всего для каждой функции предусмотрено по 2 теста с разными входными данными

- #### Circle.py
```python
class CircleTestCase(unittest.TestCase):
    def test_zero_area(self):
        expectedResult = 0
        result = circle.area(0)
        self.assertEqual(expectedResult, result)

    def test_pi_area(self):
        expectedResult = math.pi
        result = circle.area(1)
        self.assertEqual(expectedResult, result)

    def test_zero_perimeter(self):
        expectedResult = 0
        result = circle.perimeter(0)
        self.assertEqual(expectedResult, result)

    def test_one_perimeter(self):
        expectedResult = 1
        result = circle.perimeter(1 / (math.pi * 2))
        self.assertAlmostEqual(expectedResult, result)
```
- #### Square.py
```python
class SquareTestCase(unittest.TestCase):
    def test_zero_area(self):
        expectedResult = 0
        result = square.area(0)
        self.assertEqual(expectedResult, result)

    def test_area(self):
        expectedResult = 25
        result = square.area(5)
        self.assertEqual(expectedResult, result)

    def test_zero_perimeter(self):
        expectedResult = 0
        result = square.perimeter(0)
        self.assertEqual(expectedResult, result)

    def test_perimeter(self):
        expectedResult = 20
        result = square.perimeter(5)
        self.assertEqual(expectedResult, result)
```
## 5. Критерии приемки
Все тесты должны быть завершены без ошибок и успешны

## 6. Ожидаемые результаты
8 тестов должны завершиться успешно (**OK**)