# Labwork №1

## General description of the solution

The project collected functions for calculating the area and perimeter of basic planimetric figures. All functions were divided nto 4 files (for each figure). Project was creaеted for to make it easier to access mathematical formulas.

## Description of each function

8 functions were used in the project

### In the file rectangle.py

- **area(float a, float b)** - return area of rectangle with sides **a**, **b**.
  
~~~text
area(5, 10) --> 50.0
~~~

- **perimeter(float a, float b)** - return perimeter of rectangle with sides **a**, **b**.
  
~~~text
perimeter(5, 10) --> 30.0
~~~

### In the file circle.py

- **area(float r)** - return area of circle with radius **r** rounded to the nearest whole.

~~~text
area(5) --> 79
~~~

- **perimeter(float r)** - return perimeter of circle with radius **r** rounded to the nearest whole
  
~~~text
perimeter(5) --> 31
~~~

### In the file square.py

- **area(float a)** - return area of square with side **a**

~~~text
area(5) --> 25.0
~~~

- **perimeter(float a)** - return perimeter of square with side **a**

~~~text
perimeter(5) --> 20.0
~~~

### In the file triangle.py

- **area(float a, float h)** - return area of triangle with side **a** and height **h**

~~~text
area(5, 10) --> 25.0
~~~

- **perimeter(float a, float b, float c)** - return perimeter of triangle with sides **a**, **b**, **c**

~~~text
perimter(1, 2, 3) --> 6.0
~~~

## The story of commits

1. The project was created.
2. rectangle.py were added in project.
3. First commit

     ~~~text
     git commit -m "added a new file rectangle.py"
     ~~~

4. triangle.py were added in project. Bugs have been fixed in rectangle.py.
5. Secong commit

    ~~~text
    git commit -m "fixed bugs in rectangle.py and added triangle.py"
    ~~~

### Hashes of commits

![picture not found](https://sun9-5.userapi.com/impg/FqALz2c9iPK72eD7_Uws1fvEijKcT_Hkcbe9PA/2viVLLKt2VY.jpg?size=517x190&quality=96&sign=da61e2d6fc30e7ec1ff35a11ec67e560&type=album)

## Tests

Added groups of tests for rectangle, triangle, circle and square.

### Rectangle

#### area

|Group of tests|Works correctly|Expected result|Real Result|Date|
|--------------|---------------|-----------------|----------------------------|-------------------------|
|test_area_normal|✅|result by math formula|result by math formula|06.11.2023|
|test_area_strings|❌|exception|result by Python|06.11.2023|
|test_area_negative|❌|exception|result by formula|06.11.2023|
|test_area_zero_mul|❌|exception|result by formula|06.11.2023|
|test_area_objects|✅|exception|exception|06.11.2023|

#### perimeter

|Group of tests|Works correctly|Expected result|Real Result|Date|
|--------------|---------------|-----------------|----------------------------|-------------------------|
|test_perimeter_normal|✅|result by math formula|result by math formula|06.11.2023|
|test_perimeter_strings|❌|exception|result by Python|06.11.2023|
|test_perimeter_negative|❌|exception|result by formula|06.11.2023|
|test_perirmeter_zero_mul|❌|exception|result by formula|06.11.2023|
|test_perimeter_objects|✅|exception|exception|06.11.2023|

### Square

#### area

|Group of tests|Works correctly|Expected result|Real Result|Date|
|--------------|---------------|-----------------|----------------------------|-------------------------|
|test_area_normal|✅|result by math formula|result by math formula|06.11.2023|
|test_area_strings|✅|exception|exception|06.11.2023|
|test_area_not_positive|❌|exception|result by formula|06.11.2023|
|test_area_objects|✅|exception|exception|06.11.2023|

#### perimeter

|Group of tests|Works correctly|Expected result|Real Result|Date|
|--------------|---------------|-----------------|----------------------------|-------------------------|
|test_area_normal|✅|result by math formula|result by math formula|06.11.2023|
|test_area_strings|❌|exception|result by Python|06.11.2023|
|test_area_not_positive|❌|exception|result by formula|06.11.2023|
|test_area_objects|✅|exception|exception|06.11.2023|

### Circle

#### area

|Group of tests|Works correctly|Expected result|Real Result|Date|
|--------------|---------------|-----------------|----------------------------|-------------------------|
|test_area_normal|✅|result by math formula|result by math formula|06.11.2023|
|test_area_strings|✅|exception|exception|06.11.2023|
|test_area_negative|❌|exception|result by formula|06.11.2023|
|test_area_objects|✅|exception|exception|06.11.2023|

#### perimeter

|Group of tests|Works correctly|Expected result|Real Result|Date|
|--------------|---------------|-----------------|----------------------------|-------------------------|
|test_area_normal|✅|result by math formula|result by math formula|06.11.2023|
|test_area_strings|✅|exception|exception|06.11.2023|
|test_area_negative|❌|exception|result by formula|06.11.2023|
|test_area_objects|✅|exception|exception|06.11.2023|

### Triangle

#### area

|Group of tests|Works correctly|Expected result|Real Result|Date|
|--------------|---------------|-----------------|----------------------------|-------------------------|
|test_area_normal|✅|result by math formula|result by math formula|06.11.2023|
|test_area_strings|✅|exception|exception|06.11.2023|
|test_area_negative|❌|exception|result by formula|06.11.2023|
|test_area_zero_mul|❌|exception|result by formula|06.11.2023|
|test_area_objects|✅|exception|exception|06.11.2023|

#### perimeter

|Group of tests|Works correctly|Expected result|Real Result|Date|
|--------------|---------------|-----------------|----------------------------|-------------------------|
|test_area_normal|✅|result by math formula|result by math formula|06.11.2023|
|test_perimeter_incorrect|❌|result by triangle inequality theorem|result by formula|06.11.2023|
|test_area_strings|❌|exception|result by Python|06.11.2023|
|test_area_negative|❌|exception|result by formula|06.11.2023|
|test_area_zero_mul|❌|exception|result by formula|06.11.2023|
|test_area_objects|✅|exception|exception|06.11.2023|

## Math formulas

### Area

- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: S = a * h / 2

### Perimeter

- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle: P = a + b + c
  