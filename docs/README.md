## Результаты тестирования
В ходе тестирования вывлено, что программа работает правильно только при логически верных входных данных (положительных целых и вещественных значениях), в функции стоит добавить проверку входных данных, для выведения ошибки, при попытке пользователя ввести отрицательные значения или иные символы, не являющиеся числами.
| Файл | Тест | Входные данные | Ожидаемый результат | Полученный результат | Статус |
|------------|------|----------------|---------------------|----------------------|--------|
| circle.py  | area() | 8 | 201.06192982974676 | 201.06192982974676 | correct |
| circle.py  | area() | 9.31 | 272.30099900181426 | 272.30099900181426 | correct |
| circle.py  | area() | -15 | Error error invalid value entered | error | invalid value entered |
| circle.py  | area() | 0 | 0 | 0 | correct |
| circle.py  | area() | 8 | 201.06192982974676 | 201.06192982974676 | Верно |
| circle.py  | area() | 9.31 | 272.30099900181426 | 272.30099900181426 | Верно |
| circle.py  | area() | -15 | 706.8583470577034 | 706.8583470577034 | Верно |
| circle.py  | area() | 0 | 0 | 0 | Верно |
| circle.py  | perimeter() | 8 | 50.26548245743669 | 50.26548245743669 | correct |
| circle.py  | perimeter() | 9.31 | 58.49645520984195 | 58.49645520984195 | correct |
| circle.py  | perimeter() | -15 | error | error | invalid value entered |
| circle.py  | perimeter() | 0 | 0 | 0 | correct |
| circle.py  | perimeter() | 8 | 50.26548245743669 | 50.26548245743669 | Верно |
| circle.py  | perimeter() | 9.31 | 58.49645520984195 | 58.49645520984195 | Верно |
| circle.py  | perimeter() | -15 | -94.24777960769379 | -94.24777960769379 | Верно |
| circle.py  | perimeter() | 0 | 0 | 0 | Верно |
| square.py  | area() | 3 | 9 | 9 | correct |
| square.py  | area() | -99 | error | error | invalid value entered |
| square.py  | area() | 16.77 | 281.2329 | 281.2329 | correct |
| square.py  | area() | 0 | 0 | 0 | correct |
| square.py  | area() | 3 | 9 | 9 | Верно |
| square.py  | area() | -99 | 9801 | 9801 | Верно |
| square.py  | area() | 16.77 | 281.2329 | 281.2329 | Верно |
| square.py  | area() | 0 | 0 | 0 | Верно |
| square.py  | perimeter() | 3 | 12 | 12 | correct |
| square.py  | perimeter() | -99 | error | error | invalid value entered |
| square.py  | perimeter() | 16.77 | 67.08 | 67.08 | correct |
| square.py  | perimeter() | 0 | 0 | 0 | correct |
| square.py  | perimeter() | 3 | 12 | 12 | Верно |
| square.py  | perimeter() | -99 | -396 | -396 | Верно |
| square.py  | perimeter() | 16.77 | 67.08 | 67.08 | Верно |
| square.py  | perimeter() | 0 | 0 | 0 | Верно |
| triangle.py  | area() | 3 | 6 | 9 | 9 | correct |
| triangle.py  | area() | -7 | 12 | error | error | invalid value entered |
| triangle.py  | area() | 3.5 | 6.8 | 11.9 | 11.9 | correct |
| triangle.py  | area() | 12.1 | 8 | 48.2 | 48.2 | correct |
| triangle.py  | area() | 3 | 6 | 9 | 9 | Верно |
| triangle.py  | area() | -7 | 12 | -42 | -42 | Верно |
| triangle.py  | area() | 3.5 | 6.8 | 11.9 | 11.9 | Верно |
| triangle.py  | area() | 12.1 | 8 | 48.2 | 48.2 | Верно |
| triangle.py  | perimeter() | 4 | 3 | 5 | 12 | 12 | correct |
| triangle.py  | perimeter() | -12 | 4 | 8 | error | error | invalid value entered |
| triangle.py  | perimeter() | 0 | 98 | 0 | error | error | invalid value entered |
| triangle.py  | perimeter() | 9.766 | 16 | 9.01 | 34.775999999999996 | 34.775999999999996 | correct |
| triangle.py  | perimeter() | 4 | 3 | 5 | 12 | 12 | Верно |
| triangle.py  | perimeter() | -12 | 4 | 8 | 0 | 0 | Верно |
| triangle.py  | perimeter() | 0 | 98 | 0 | 98 | 98 | Верно |
| triangle.py  | perimeter() | 9.766 | 16 | 9.01 | 34.775999999999996 | 34.775999999999996 | Верно |
| rectangle.py  | area() | 5 | -7 | error | error | invalid value entered |
| rectangle.py  | area() | 8 | 13.5 | 108 | 108 | correct |
| rectangle.py  | area() | 1 | 3 | 3 | 3 | correct |
| rectangle.py  | area() | 0 | 89 | 0 | 0 | correct |
| rectangle.py  | area() | 5 | -7 | error | error | invalid value entered |
| rectangle.py  | area() | 8 | 13.5 | 43 | 43 | Верно |
| rectangle.py  | area() | 1 | 3 | 8 | 8 | Верно |
| rectangle.py  | area() | 0 | 89 | error | error | invalid value entered |
