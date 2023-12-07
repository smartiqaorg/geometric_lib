# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle S = a * h * 0.5
## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle S = a + b + c

## Описание 

### main.yml:
#### Runner'ы:
- ubuntu-latest
```angular2html
Запускает автотесты на виртуальной машине с операционной системой Ubuntu. 
```

- windows-latest
```angular2html
Запускает автотесты на виртуальной машине с операционной системой Windows. 
```
 
В каждом из runner'ов устанавливается Python 3.12, а также указывается архитектура x64. Далее запускаются unit-тесты.