# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a

## Python usage

Run Python 3 from the repository root to import the modules available on `main`.
For a circle, pass its radius; for a square, pass its side length.

```python
import circle
import square

print(round(circle.area(2), 5))       # 12.56637
print(round(circle.perimeter(2), 5))  # 12.56637
print(square.area(3))                # 9
print(square.perimeter(3))           # 12
```
