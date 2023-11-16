# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a

# Тестирование
Создан класс MyTest(unittest.TestCase) в котором прописаны unit тесты
+ test_square_area - тестирование функции square.area
+ test_square_perimeter - тестирование функции square.perimeter
+ test_triangle_area - тестирование функции triangle.area
+ test_triangle_perimeter - тестирование функции triangle.perimeter
+ test_circle_area - тестирование функции circle.area
+ test_circle_perimeter - тестирование функции circle.perimeter
+ test_rectangle_area - тестирование функции rectangle.area
+ test_rectangle_perimeter - тестирование функции rectangle.perimeter
## Тест-кейсы
<table>
  <thead>
    <tr>
      <th>тестируемая функция</th>
      <th>входные данные</th>
      <th>ожидаемый результат</th>
      <th>результат теста</th>
    </tr>

  </thead>
  <tbody>
    <tr>
      <td>square.area</td>
      <td>3</td>
      <td>9</td>
      <td>ok</td>
    </tr>
    <tr>
      <td>square.area</td>
      <td>0</td>
      <td>0</td>
      <td>ok</td>
    </tr>
    <tr>
      <td>square.area</td>
      <td>-1</td>
      <td>1</td>
      <td>ok</td>
    </tr>
    <tr>
      <td>square.area</td>
      <td>100</td>
      <td>10000</td>
      <td>ok</td>
    </tr>
    <tr>
      <td>square.area</td>
      <td>1.3</td>
      <td>1.69</td>
      <td>ok</td>
    </tr>
    <tr>
      <td>square.area</td>
      <td>"hello"</td>
      <td>TypeError</td>
      <td>ok</td>
    </tr>
    <tr>
      <td>square.area</td>
      <td>20000</td>
      <td>400000000</td>
      <td>ok</td>
    </tr>
    <tr>
      <td>square.perimeter</td>
      <td>0</td>
      <td>0</td>
      <td>ok</td>
    </tr>
    <tr>
      <td>square.perimeter</td>
      <td>-3</td>
      <td>-12</td>
      <td>ok</td>
    </tr>
    <tr>
      <td>square.perimeter</td>
      <td>300</td>
      <td>1200</td>
      <td>ok</td>
    </tr>
    <tr>
      <td>square.perimeter</td>
      <td>2.4</td>
      <td>9.6</td>
      <td>ok</td>
    </tr>
    <tr>
      <td>square.perimeter</td>
      <td>sin(0)</td>
      <td>0</td>
      <td>ok</td>
    </tr>
    <tr>
      <td>square.perimeter</td>
      <td>ceil(3.2)</td>
      <td>16</td>
      <td>ok</td>
    </tr>
    <tr>
      <td>triangle.area</td>
      <td>2, 3</td>
      <td>3</td>
      <td>ok</td>
    </tr>
    <tr>
      <td>triangle.area</td>
      <td>0, 0</td>
      <td>0</td>
      <td>ok</td>
    </tr>
    <tr>
      <td>triangle.area</td>
      <td>3, 3</td>
      <td>4.5</td>
      <td>ok</td>
    </tr>
    <tr>
      <td>triangle.area</td>
      <td>3, -1</td>
      <td>-1.5</td>
      <td>ok</td>
    </tr>
    <tr>
      <td>triangle.area</td>
      <td>600, 1</td>
      <td>300</td>
      <td>ok</td>
    </tr>
    <tr>
      <td>triangle.area</td>
      <td>5.1, 2.3</td>
      <td>5.1*2.3/2</td>
      <td>ok</td>
    </tr>
    <tr>
      <td>triangle.perimeter</td>
      <td>1, 2, 3</td>
      <td>6</td>
      <td>ok</td>
    </tr>
    <tr>
      <td>triangle.perimeter</td>
      <td>3, -2, 6</td>
      <td>7</td>
      <td>ok</td>
    </tr>
    <tr>
      <td>triangle.perimeter</td>
      <td>1031, 0, 245</td>
      <td>1276</td>
      <td>ok</td>
    </tr>
    <tr>
      <td>triangle.perimeter</td>
      <td>0, 0, 0</td>
      <td>0</td>
      <td>ok</td>
    </tr>
    <tr>
      <td>triangle.perimeter</td>
      <td>𝝅, -3, 4</td>
      <td>1+𝝅</td>
      <td>ok</td>
    </tr>
    <tr>
      <td>triangle.perimeter</td>
      <td>"srt"</td>
      <td>TypeError</td>
      <td>ok</td>
    </tr>
    <tr>
      <td>circle.area</td>
      <td>0</td>
      <td>0</td>
      <td>ok</td>
    </tr>
    <tr>
      <td>circle.area</td>
      <td>0</td>
      <td>0*𝝅</td>
      <td>ok</td>
    </tr>
    <tr>
      <td>circle.area</td>
      <td>-3</td>
      <td>9*𝝅</td>
      <td>ok</td>
    </tr>
    <tr>
      <td>circle.area</td>
      <td>100</td>
      <td>10000*𝝅</td>
      <td>ok</td>
    </tr>
    <tr>
      <td>circle.area</td>
      <td>1.4</td>
      <td>1.96*𝝅</td>
      <td>ok</td>
    </tr>
    <tr>
      <td>circle.area</td>
      <td>"hello"</td>
      <td>TypeError</td>
      <td>ok</td>
    </tr>
    <tr>
      <td>circle.perimeter</td>
      <td>3</td>
      <td>6*𝝅</td>
      <td>ok</td>
    </tr>
    <tr>
      <td>circle.perimeter</td>
      <td>0</td>
      <td>0*𝝅</td>
      <td>ok</td>
    </tr>
    <tr>
      <td>circle.perimeter</td>
      <td>0</td>
      <td>0</td>
      <td>ok</td>
    </tr>
    <tr>
      <td>circle.perimeter</td>
      <td>-2</td>
      <td>-4*𝝅</td>
      <td>ok</td>
    </tr>
    <tr>
      <td>circle.perimeter</td>
      <td>2001</td>
      <td>4002*𝝅</td>
      <td>ok</td>
    </tr>
    <tr>
      <td>circle.perimeter</td>
      <td>3.5</td>
      <td>7*𝝅</td>
      <td>ok</td>
    </tr>
    <tr>
      <td>rectangle.area</td>
      <td>2, 3</td>
      <td>6</td>
      <td>ok</td>
    </tr>
    <tr>
      <td>rectangle.area</td>
      <td>0, 9</td>
      <td>0</td>
      <td>ok</td>
    </tr>
    <tr>
      <td>rectangle.area</td>
      <td>-6, 2</td>
      <td>-12</td>
      <td>ok</td>
    </tr>
    <tr>
      <td>rectangle.area</td>
      <td>e, 1</td>
      <td>e</td>
      <td>ok</td>
    </tr>
    <tr>
      <td>rectangle.area</td>
      <td>1999, 56</td>
      <td>111944</td>
      <td>ok</td>
    </tr>
    <tr>
      <td>rectangle.perimeter</td>
      <td>3, 4</td>
      <td>14</td>
      <td>ok</td>
    </tr>
    <tr>
      <td>rectangle.perimeter</td>
      <td>0, 2</td>
      <td>4</td>
      <td>ok</td>
    </tr>
    <tr>
      <td>rectangle.perimeter</td>
      <td>-5, -2</td>
      <td>-14</td>
      <td>ok</td>
    </tr>
    <tr>
      <td>rectangle.perimeter</td>
      <td>-4, 4</td>
      <td>0</td>
      <td>ok</td>
    </tr>
    <tr>
      <td>rectangle.perimeter</td>
      <td>2.5, 3.5</td>
      <td>12</td>
      <td>ok</td>
    </tr>
    <tr>
      <td>rectangle.perimeter</td>
      <td>"loex"</td>
      <td>TypeError</td>
      <td>ok</td>
    </tr>
  </tbody>
</table>
