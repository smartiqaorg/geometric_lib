# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a

# General description of the solution

**Geometric Lib** is a Python library for calculating
the area and perimeter of basic geometric shapes: circle and square.

Each shape is placed in a separate module (`circle.py `, `square.py `) and contains two functions:

- `area(...)` — calculates the area of the shape
- `perimeter(...)`— calculates the perimeter of the shape

# Function descriptions

## circle.py

A module for calculating circle parameters.

### `area(r)`

Calculates the area of a circle using the formula **S = π·r2**.

**Parameters:**
- `r` (float) is the radius of the circle.

**Returns:** 
- `float` — the area of the circle.

**Example:**

```python
from circle import area

result = area(5)
print(result)   # 78.53981633974483
```

### `perimeter(r)`

Calculates the circumference using the formula **P = 2·π·r**.

**Parameters:**
- `r` (float) is the radius of the circle.

**Returns:** 
- `float` — the circumference.

**Example:**

```python
from circle import perimeter

result = perimeter(5)
print(result)   # 31.41592653589793
```

---


## square.py

A module for calculating the parameters of a square.

### `area(a)`

Calculates the area of a square using the formula **S = a²**.

**Parameters:**
- `a` (float) — the length of the square's side.

**Returns:** 
- `float` — the area of the square.

**Example:**

```python
from square import area

result = area(6)
print(result)   # 36
```

### `perimeter(a)`

Calculates the perimeter of a square using the formula **P = 4·a**.

**Parameters:**
- `a` (float) — the length of a side of the square.

**Returns:** 
- `float` — the perimeter of the square.

**Example:**

```python
from square import perimeter

result = perimeter(4)
print(result)   # 16
```

---

# The history of changes to the project with commit hashes
- 8ba9aeb L-03: Circle and square added
- d078c8d (origin/main, origin/HEAD, main) L-03: Docs added
- 13e12e4 (new_features_558152) gfd
- 8eb42d3 (HEAD -> docs_558152) square.py and circle.py were added with dockstrings

---