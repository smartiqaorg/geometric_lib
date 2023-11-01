##### The library contains functions that can be used to calculate the areas and perimeters of some geometric figures
# Math formulas used

|                             | **Area** | **Perimeter** |
|-----------------------------|:--------:|:-------------:|
| **[circle](#Circle)**       |   πR²    |      2πR      |
| **[rectangle](#Rectangle)** |    ab    |    2a + 2b    |
| **[square](#Square)**       |    a²    |      4a       |
| **[triangle](#Triangle)**   | 1/2(ah)  |   a + b + c   |

---
# Functions description
## Circle
#### `def area(r)`

Accepts circle radius (int), returns circle area (int).

    Example:

        input: 10
        output: 314.1592653589793

#### `def perimeter(r)`
Accepts circle radius (int), returns circumference (int).

    Example:

        input: 10
        output: 62.83185307179586


---
## Rectangle
#### `def area(a,b)`
Accepts rectangle sides, returns rectangle area.

        Parameters:

            a (int) : side a of a rectangle
            b (int) : side b of a rectangle

        Returns:

            a * b (int) : rectangle area

        Example:

            input: 2 5
            output: 10

#### `def perimeter(a,b)`
Accepts rectangle sides, returns rectangle perimeter.

        Parameters:

            a (int) : side a of a rectangle
            b (int) : side b of a rectangle

        Returns:

            2*(a + b) (int) : rectangle perimeter

        Example:

            input: 2 5
            output: 14

---
## Square
#### `def area(a)`
Accepts square side (int), returns square area (int).

        Example:

            input: 10
            output: 100

#### `def perimeter(a)`
Accepts square side (int), returns square perimeter (int).

        Example:

            input: 10
            output: 40

---
## Triangle
#### `def area(a,b)`
Accepts triangle height and base side, returns triangle area.

        Parameters:

            a (int) : base side of a triangle
            b (int) : height of a triangle

        Returns:

            a * h / 2 (int) : triangle area

        Example:

            input: 5 10
            output: 25.0

#### `def perimeter(a,b)`
Accepts triangle sides, returns triangle perimeter.

        Parameters:

             a (int) : side a of a triangle
             b (int) : side b of a triangle
             c (int) : side c of a triangle

        Returns:

             a + b + c : perimeter (int)

        Example:

             input: 1 2 3
             output: 6

---
# Project history

- 8ba9aeb L-03: Circle and square added
- d078c8d (upstream/main, upstream/HEAD) L-03: Docs added
- 3575695 added a new file
- f2e9748 (origin/main, origin/HEAD, main) fixed a mistake in rectangle.py
- 6d17900 (HEAD -> new_features_412963) commented all of the functions
- c2094bc added a unit test file for each source file. The following commits are describing tests implementation