# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle S = a * h * 0.5
## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle S = a + b + c


## Tests

| Номер теста | Название модуля  | Название функции  | Входные данные для функции       | Полученный результат | Ожидаемый результат | Вердикт    |
|-------------|------------------|-------------------|----------------------------------|----------------------|---------------------|------------|
| 1           | circle           | area              | radius=0                         | 0                    | 0                   | Passed     |
| 2           | circle           | area              | radius=10                        | 314.1592653589793    | 314.1592653589793   | Passed     |
| 3           | circle           | area              | radius=2.5                       | 19.634954084936208   | 19.634954084936208  | Passed     |
| 4           | circle           | perimeter         | radius=0                         | 0                    | 0                   | Passed     |
| 5           | circle           | perimeter         | radius=10                        | 62.83185307179586    | 62.83185307179586   | Passed     |
| 6           | circle           | perimeter         | radius=2.5                       | 15.707963267948966   | 15.707963267948966  | Passed     |
| 7           | rectangle        | area              | length=10, width=0               | 0                    | 0                   | Passed     |
| 8           | rectangle        | area              | length=10, width=20              | 200                  | 200                 | Passed     |
| 9           | rectangle        | area              | length=3.5, width=2.5            | 8.75                 | 8.75                | Passed     |
| 10          | rectangle        | perimeter         | length=0, width=0                | 0                    | 0                   | Passed     |
| 11          | rectangle        | perimeter         | length=10, width=20              | 60                   | 60                  | Passed     |
| 12          | rectangle        | perimeter         | length=3.5, width=2.5            | 12                   | 12                  | Passed     |
| 13          | square           | area              | side=0                           | 0                    | 0                   | Passed     |
| 14          | square           | area              | side=10                          | 100                  | 100                 | Passed     |
| 15          | square           | area              | side=2.5                         | 6.25                 | 6.25                | Passed     |
| 16          | square           | perimeter         | side=0                           | 0                    | 0                   | Passed     |
| 17          | square           | perimeter         | side=10                          | 40                   | 40                  | Passed     |
| 18          | square           | perimeter         | side=2.5                         | 10                   | 10                  | Passed     |
| 19          | triangle         | area              | base=0, height=0                 | 0                    | 0                   | Passed     |
| 20          | triangle         | area              | base=10, height=8                | 40                   | 40                  | Passed     |
| 21          | triangle         | area              | base=2.5, height=3.5             | 4.375                | 4.375               | Passed     |
| 22          | triangle         | perimeter         | side1=0, side2=0, side3=0        | 0                    | 0                   | Passed     |
| 23          | triangle         | perimeter         | side1=10, side2=10, side3=12     | 32                   | 32                  | Passed     |
| 24          | triangle         | perimeter         | side1=2.5, side2=2.5, side3=3.2  | 8.2                  | 8.2                 | Passed     |