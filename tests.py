import unittest
import square
import triangle
import circle
import rectangle
import math

class MyTest(unittest.TestCase):
    def test_square_area(self):
        """тестирование функции square.area"""
        self.assertEqual(square.area(3),9)
        self.assertEqual(square.area(0),0)
        self.assertEqual(square.area(-1),1)
        self.assertEqual(square.area(100),10000)
        self.assertEqual(square.area(1.3),1.3*1.3)
        self.assertRaises(TypeError, square.area,"hello")
        self.assertEqual(square.area(20000),400000000)

    def test_square_perimeter(self): 
        """тестирование функции square.perimeter"""
        self.assertEqual(square.perimeter(0),0)
        self.assertEqual(square.perimeter(-3),-12)
        self.assertEqual(square.perimeter(300),1200)
        self.assertEqual(square.perimeter(2.4),9.6)
        self.assertEqual(square.perimeter(math.sin(0)),0)
        self.assertEqual(square.perimeter(math.ceil(3.2)),16)

    def test_triangle_area(self):
        """тестирование функции triangle.area"""
        self.assertEqual(triangle.area(2,3),3)
        self.assertEqual(triangle.area(0,0),0)
        self.assertEqual(triangle.area(3,3),4.5)
        self.assertEqual(triangle.area(3,-1),-1.5)
        self.assertEqual(triangle.area(600,1),300)
        self.assertEqual(triangle.area(5.1,2.3),5.1*2.3/2)

    def test_triangle_perimeter(self):
        """тестирование функции triangle.perimeter"""
        self.assertEqual(triangle.perimeter(1,2,3),6)
        self.assertEqual(triangle.perimeter(3,-2,6),7)
        self.assertEqual(triangle.perimeter(1031,0,245),1276)
        self.assertEqual(triangle.perimeter(0,0,0),0)
        self.assertEqual(triangle.perimeter(math.pi,-3,4),1+math.pi)
        self.assertRaises(TypeError, triangle.perimeter,"srt")

    def test_circle_area(self):
        """тестирование функции circle.area"""
        self.assertEqual(circle.area(0),0)
        self.assertEqual(circle.area(0),0*math.pi)
        self.assertEqual(circle.area(-3),9*math.pi)
        self.assertEqual(circle.area(100),10000*math.pi)
        self.assertEqual(circle.area(1.4),1.96*math.pi)
        self.assertRaises(TypeError, circle.area,"hello")

    def test_circle_perimeter(self):
        """тестирование функции circle.perimeter"""
        self.assertEqual(circle.perimeter(3),6*math.pi)
        self.assertEqual(circle.perimeter(0),0*math.pi)
        self.assertEqual(circle.perimeter(0),0)
        self.assertEqual(circle.perimeter(-2),-4*math.pi)
        self.assertEqual(circle.perimeter(2001),4002*math.pi)
        self.assertEqual(circle.perimeter(3.5),7*math.pi)

    def test_rectangle_area(self):
        """тестирование функции rectangle.area"""
        self.assertEqual(rectangle.area(2,3),6)
        self.assertEqual(rectangle.area(0,9),0)
        self.assertEqual(rectangle.area(-6,2),-12)
        self.assertEqual(rectangle.area(math.e,1),math.e)
        self.assertEqual(rectangle.area(1999,56),111944)

    def test_rectangle_perimeter(self):
        """тестирование функции rectangle.perimeter"""
        self.assertEqual(rectangle.perimeter(3,4),14)
        self.assertEqual(rectangle.perimeter(0,2),4)
        self.assertEqual(rectangle.perimeter(-5,-2),-14)
        self.assertEqual(rectangle.perimeter(-4,4),0)
        self.assertEqual(rectangle.perimeter(2.5,3.5),12)
        self.assertRaises(TypeError, rectangle.perimeter,"loex")
    
unittest.main()