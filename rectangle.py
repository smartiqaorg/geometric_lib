def area(a, b):
    '''
    Accepts rectangle sides, returns rectangle area.

        Parameters:
            a (int) : side a of a rectangle
            b (int) : side b of a rectangle

        Returns:
            a * b (int) : rectangle area

        Example:
            input: 2 5
            output: 10
    '''
    return a * b

def perimeter(a, b):
    '''
    Accepts rectangle sides, returns rectangle perimeter.

        Parameters:
            a (int) : side a of a rectangle
            b (int) : side b of a rectangle

        Returns:
            2*(a + b) (int) : rectangle perimeter

        Example:
            input: 2 5
            output: 14
    '''
    if a == 0 or b == 0:
        return 0
    return 2*(a + b)
