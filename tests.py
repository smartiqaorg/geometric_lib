import unittest
import circle_test, rectangle_test, square_test, triangle_test

suite1 = unittest.TestLoader().loadTestsFromModule(circle_test)
suite2 = unittest.TestLoader().loadTestsFromModule(rectangle_test)
suite3 = unittest.TestLoader().loadTestsFromModule(square_test)
suite4 = unittest.TestLoader().loadTestsFromModule(triangle_test)

unittest.TextTestRunner(verbosity=2).run(suite1)
unittest.TextTestRunner(verbosity=2).run(suite2)
unittest.TextTestRunner(verbosity=2).run(suite3)
unittest.TextTestRunner(verbosity=2).run(suite4)
