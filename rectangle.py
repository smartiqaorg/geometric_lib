def area(a, b):
    '''Returns the area of the rectangle.

            Parameters:
                a (int): first side of the rectangle
                b (int): second side og the rectangle
            Returns:
                (int): area of the rectangle
                
        Example:
            input -> 2, 3 (a, b)
            output -> 6 (a * b)
    '''

    return a * b 

def perimeter(a, b):
    '''Returns the perimeter of the rectangle.

            Parameters:
                a (int): first side of the rectangle
                b (int): second side og the rectangle
            Returns:
                (int): perimeter of the rectangle
                
        Example:
            input -> 2, 3 (a, b)
            output -> 10 (2 * (a + b))
    '''

    return 2 * (a + b)
