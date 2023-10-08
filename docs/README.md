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

![picture not found](https://sun9-10.userapi.com/impg/kS4KIKKTzoCSIvbRGdfGuZda7GC76X7MprGOJQ/o2HzeJ4o2UE.jpg?size=511x79&quality=96&sign=4d2048d250ae2e83e01b5875020f0a8b&type=album)

## Math formulas

### Area

- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

### Perimeter

- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a