import unittest
class TestRectangle(unittest.TestCase):
   def test_area_1(self):
       result = self.rectangle.area(10, 9)
       self.assertEqual(result, 90)
   def test_area_2(self):
       result = self.rectangle.area(-5, 10)
       self.assertEqual(result, 0)
   def test_area_3(self):
       res = self.rectangle.area(13, 0)
       self.assertEqual(res, 0)
   def test_area_4(self):
       res = self.rectangle.area(-14, -10)
       self.assertEqual(res, 0)
   def test_perimeter_1(self):
       result = self.rectangle.perimeter(10, 9)
       self.assertEqual(result, 38)
   def test_perimeter_2(self):
       result = self.rectangle.perimeter(-5, 10)
       self.assertEqual(result, 0)
   def test_perimeter_3(self):
       res = self.rectangle.perimeter(13, 0)
       self.assertEqual(res, 0)
   def test_perimeter_4(self):
       res = self.rectangle.perimeter(-14, -10)
       self.assertEqual(res, 0)
if __name__ == "__main__":
    unittest.main()
