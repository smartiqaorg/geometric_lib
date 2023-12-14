# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a


## Tests

| Номер теста | Название модуля  | Название функции  | Входные данные для функции    | Полученный результат | Ожидаемый результат | Вердикт				    |
|-------------|------------------|-------------------|------------------------------ |----------------------|---------------------|-------------------------|
| 1           | circle           | area              | radius=8                      | 201.06192982974676   | 201.062			  | Passed, delta=0.001     |
| 2           | circle           | area              | radius=4                      | 50.26548245743669    | 50.266			  | Passed, delta=0.001     |
| 3           | circle           | area              | radius=-34                    | 3631.6811075498013   | ValueError		  | Failed				    |
| 3           | circle           | area              | radius="str"                  | TypeError			   | TypeError		  | Passed				    |
| 4           | circle           | perimeter         | radius=4                      | 25.132741228718345   | 25.133			  | Passed, delta=0.001     |
| 5           | circle           | perimeter         | radius=8                      | 50.26548245743669    | 50.266			  | Passed, delta=0.001     |
| 6           | circle           | perimeter         | radius=-15                    | -94.24777960769379   | ValueError		  | Failed, delta=0.001     |
| 6           | circle           | perimeter         | radius="str"                  | TypeError			   | TypeEerror		  | Passed				    |
| 7           | rectangle        | area              | length=8, width=9             | 72                   | 72                  | Passed				    |
| 8           | rectangle        | area              | length=3, width=7             | 21                   | 21                  | Passed				    |
| 9           | rectangle        | area              | length=-2, width=89           | -178                 | ValueError          | Failed				    |
| 9           | rectangle        | area              | length=-2, width="str"        | TypeError            | TypeError			  | Passed				    |
| 10          | rectangle        | perimeter         | length=9.4, width=8           | 34.8                 | 34.8                | Passed				    |
| 11          | rectangle        | perimeter         | length=10, width=12           | 44                   | 44                  | Passed				    |
| 12          | rectangle        | perimeter         | length=-6, width=84           | 156                  | ValueError          | Failed				    |
| 12          | rectangle        | perimeter         | length=-6, width="str"        | TypeError            | TypeError           | Passed				    |
| 13          | square           | area              | side=5                        | 25                   | 25                  | Passed				    |
| 14          | square           | area              | side=3                        | 9                    | 9                   | Passed				    |
| 15          | square           | area              | side=-6.2                     | 38.44                | ValueError          | Failed				    |
| 15          | square           | area              | side="str"                    | TypeError            | TypeError           | Passed				    |
| 16          | square           | perimeter         | side=3                        | 12                   | 12                  | Passed				    |
| 17          | square           | perimeter         | side=10                       | 40                   | 40                  | Passed				    |
| 18          | square           | perimeter         | side=-5.5                     | -22                  | ValueError          | Failed				    |
| 18          | square           | perimeter         | side="str"                    | TypeError            | TypeError           | Passed				    |
| 19          | triangle         | area              | base=8, height=4              | 16                   | 16                  | Passed				    |
| 20          | triangle         | area              | base=3, height=10             | 15                   | 15                  | Passed				    |
| 21          | triangle         | area              | base=-2, height=2             | -2                   | ValueError          | Failed				    |
| 21          | triangle         | area              | base=2, height="str"          | TypeError            | TypeError           | Passed				    |
| 22          | triangle         | perimeter         | side1=3, side2=4, side3=5     | 12                   | 12                  | Passed				    |
| 23          | triangle         | perimeter         | side1=10, side2=12, side3=18  | 40                   | 40                  | Passed				    |
| 24          | triangle         | perimeter         | side1=-8, side2=8, side3=9    | 9                    | ValueError          | Failed				    |
| 24          | triangle         | perimeter         | side1="str", side2=8, side3=9 | TypeError            | TypeError           | Passed				    |
