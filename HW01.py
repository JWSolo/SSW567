'''
Created: 2020-01-22 17:58:31
Author : Jia Wen
Email : jwen6@stevens.edu
Description: Classify triangles
            equilateral triangles have all three sides with the same length
            sosceles triangles have two sides with the same length
            scalene triangles have three sides with different lengths
            right triangles have three sides with lengths, a, b, and c where a * a + b * b = c * c
'''

import unittest

def classify_triangle(a,b,c):
    """A function that can classify the type of one triangle with three numbers."""
    
    #To make sure these three numbers can make up a triangle.
    if a + b > c and b + c > a and a + c > b:
        l = list()
        l.append(a)
        l.append(b)
        l.append(c)
        new_list = sorted(l)
        if new_list[0] * new_list[0] + new_list[1] * new_list[1] == new_list[2] * new_list[2]:
            print(f"{a}, {b}, {c} can make up Right triangle.")
            return 1

        if a == b == c:
            print(f"{a}, {b}, {c} can up Equilateral triangle.")
            return 2

        if a == b or a == c or b == c:
            print(f"{a}, {b}, {c} can make up Isosceles triangle.")
            return 3

        if a != b != c:
            print(f"{a}, {b}, {c} can make up Scalene triangle.")
            return 4
    else:
        print(f"{a}, {b}, {c} Can Not make up the triangle")
        return 5
        
class TestFunction(unittest.TestCase):
    """Unit Test"""

    def test_classify_triangle(self):
         """test function working correctly."""
         self.assertTrue(classify_triangle(5,3,4) == 1)#1 means the three numbers can make up RIGHT triangle.
         self.assertEqual(classify_triangle(1,1,1),2)#2 means the three numbers can make up EQUILATERAL triangle.
         self.assertEqual(classify_triangle(6,10,6),3)#3 means the three numbers can make up ISOSCELES triangle.
         self.assertEqual(classify_triangle(2,4,3),4)#4 means the three numbers can make up SCALENE triangle.
         self.assertEqual(classify_triangle(1,2,3),5)#5 means the three numbers CAN NOT make up the triangle.
         self.assertEqual(classify_triangle(1.2,2.1,3.2),4)#check if the function with decimal numbers.
         self.assertNotEqual(classify_triangle(6,9,10),5)


if __name__ == "__main__":
    unittest.main()