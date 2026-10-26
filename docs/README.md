# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a

## Quick start (Python 3)

Clone the repository and run Python from its root directory so that the
`circle` and `square` modules can be imported. No third-party packages are needed.
All dimensions passed to a function should use the same unit; areas are
returned in squared units and perimeters in the original unit.

```python
import circle
import square

print(round(circle.area(2), 2))       # 12.57
print(round(circle.perimeter(2), 2))  # 12.57
print(square.area(3))                # 9
print(square.perimeter(3))           # 12
```
