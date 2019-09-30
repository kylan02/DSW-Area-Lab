import math #math library has pre-written math
import unittest

def circleArea(radius): 
    """Returns the area of a circle"""
    return math.pi * radius * radius

def rectArea(base, height):
    return base * height

def trapArea(base1, base2, height):
    return ((base1 + base2)/2) * height

def triArea(base,height):
    return (base * height)/2
    
	
class MyTest(unittest.TestCase):
    def testCircleArea(self):
        self.assertEqual(circleArea(5), 25*math.pi)
    def testRectArea(self):
        self.assertEqual(rectArea(5, 10), 50)
    def testTrapArea(self):
        self.assertEqual(trapArea(5, 15, 10), 100)
    def testTriArea(self):
        self.assertEqual(triArea(10, 10), 50)
    