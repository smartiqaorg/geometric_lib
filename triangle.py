def area(a, h): 
    '''Returns the area of the triangle.

            Parameters:
                a (int): base of the triangle
                h (int): height of the triangle
            Returns:
                (int): area of the triangle
                
        Example:
            input -> 5, 4 (a, h)
            output -> 10 (a * h / 2)
    '''
    return a * h / 2

def perimeter(a, b, c):
    '''Returns the perimeter of the triangle.

            Parameters:
                a (int): first side of the triangle
                b (int): second side of the triangle
                c (int): third side if the triangle
            Returns:
                (int): perimeter of the triangle
                        
        Example:
            input -> 1, 2, 3 (a, b, c)
            output -> 6 (a + b + c)
    '''

    return a + b + c 
