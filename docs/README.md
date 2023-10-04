SQUARE A*B

```
#include <stdio.h>

int main() {

    // Вызываем функцию square с аргументами 4 и 5, результат сохраняем в переменной result.
    int result = square(4, 5);
    //Выводим на печать в консоль результат умножения.
    printf("Результат: %d\n", result);
    // Завершаем функцию с возвращением статуса 0
    return 0;
}


 //Функция square принимает два аргумента целочисленного типа и возвращает результат их умножения.
int square(int a, int b) {
    return a*b;
}
Changelog:
        - **[fcc824eeadfa2097cf9c806f17dc2052206ea85e]** Create main.c
        - **[07e8a2c7376fcc929c5f5debb5b06ec8bacf74bd]** Update main.c
	- **[98dce6bdb77c4976b12c0d6d47c008702925842f]** Fix
```