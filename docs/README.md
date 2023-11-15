# Math formulas

---

Hello! This documentation will teach you how to **create functions** to **find the area and perimeter** of shapes with **python**. Let's go!

---

## Constents

---

Here you can easily find the information you need:

##### - _Circle_ [-> click here](#circle)

##### - _Rectangle_ [-> click here](#rectangle)

##### - _Square_ [-> click here](#square)

##### - _Story of changes in the project_ [-> click here](#commitANDhash)

---

### Circle <a id = "circle"></a>

---

#### - Area:

---

Firstly, for **an exact answer** you must include the **math library** to use π:

```
from math import pi
```

Next, we write a function that will take **R** (the radius of the circle) and return the area:

```
def area(R):
    return pi * r * r
```

For example:

```
R = 5
def area(5):
    return 3.141592653589793 * 5 * 5

print(area(5))
```

```
-> 78.53981633974483
```

We can use function **round( )**, which will round your answer up:

```
print(round(area(5)))
-> 79
```

---

#### - Perimeter:

---

Just like in finding the area, we will need the math library for a more accurate answer:

```
from math import pi
```

And next, we write a function that will take **R** (the radius of the circle) and return the perimetr:

```
def perimeter(R):
    return 2 * pi * R
```

For example:

```
R = 7
def perimeter(7):
    return 2 * 3.141592653589793 * 7

print(perimeter(7))
```

```
-> 43.982297150257104
```

Round our answer:

```
print(round(perimeter(7)))
-> 44
```

---

### Rectangle <a id = "rectangle"></a>

---

#### - Area:

---

Let's write a function that takes as input the values **a** and **b** (where a and b are the lengths of the sides of the rectangle). A returns **a \* b**:

```
def area(a, b):
    return a * b
```

For example:

```
a = 3
b = 4

def area(3, 4):
    return 3 * 4

print(area(3, 4))
```

```
-> 12
```

---

### - Perimeter:

---

To find the perimeter we will have to slightly modify our conclusion from function for area:

```
def area(a, b):
    return (a + b) * 2
```

For example:

```
a = 19
b = 50

def perimeter(19, 50):
    return (19 + 50) * 2

print(area(19, 50))
```

```
-> 138
```

---

### Square <a id = "square"></a>

---

#### - Area:

---

A square is a geometric figure whose sides are equal. Therefore, our function will take one variable **a**. And output **area = a \* a**:

```
def area(a):
    return a * a
```

For example:

```
a = 11

def area(11):
    return 11 * 11

print(area(11))
```

```
-> 121
```

---

#### - Perimeter:

---

To find the perimeter of a square, we need to multiply a (it's side) by 4, since the sides are equal to each other:

```
def perimeter(a):
    return a * 4
```

For example:

```
a = 41

def area(41):
    return 41 * 4

print(area(41))
```

```
-> 164
```

---

That's all. Now you know how to find the area and perimeter of such shapes as circles, rectangles and squares. Thank you for your attention!

---

### Story of changes in the project <a id = "commitANDhash"></a>

| hash    |      commit       |
| :------ | :---------------: |
| 776fb7b | add rectangle.py  |
| dfadd34 | fix rectangle.py  |
| 8fb0692 | docs rectangle.py |
| ec8937e | docs triangle.py  |
