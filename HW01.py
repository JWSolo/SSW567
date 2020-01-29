"""
Created: 2020-01-22 17:58:31
Author : Jia Wen
Email : jwen6@stevens.edu
Description: Classify triangles
            equilateral triangles have all three sides with the same length
            isosceles triangles have two sides with the same length
            scalene triangles have three sides with different lengths
            right triangles have three sides with lengths, a, b, and c where a * a + b * b = c * c
"""

import unittest


def classify_triangle(a, b, c):
    """A function that can classify the type of one triangle with three numbers."""

    # To make sure these three numbers can make up a triangle.
    if a + b > c and b + c > a and a + c > b:
        l = list()
        l.append(a)
        l.append(b)
        l.append(c)
        new_list = sorted(l)
        if new_list[0] * new_list[0] + new_list[1] * new_list[1] == new_list[2] * new_list[2]:
            return(f"{a}, {b}, {c} can make up Right triangle.")

        if a == b == c:
            return(f"{a}, {b}, {c} can up Equilateral triangle.")

        if a == b or a == c or b == c:
            return(f"{a}, {b}, {c} can make up Isosceles triangle.")

        if a != b != c:
            return(f"{a}, {b}, {c} can make up Scalene triangle.")

    else:
        return(f"{a}, {b}, {c} Can Not make up the triangle.")

class TextFunction(unittest.TestCase):
    """Unit Test"""

    def test_classify_triangle(self):
        """unit test to check classify triangle function"""
        self.assertTrue(classify_triangle(5,4,3),"5, 4, 3 can make up Right triangle.")
        self.assertTrue(classify_triangle(1,1,1),"1, 1, 1 can up Equilateral triangle.")
        self.assertTrue(classify_triangle(1,2,3),"1, 2, 3 Can Not make up the triangle.")
        self.assertTrue(classify_triangle(6,6,10),"6, 6, 10 can make up Isosceles triangle.")
        self.assertTrue(classify_triangle(4,2,3),"4, 2, 3 can make up Scalene triangle.")

if __name__ == "__main__":
    print(classify_triangle(5,4,3))
    print(classify_triangle(1,1,1))
    print(classify_triangle(1,2,3))
    print(classify_triangle(6,6,10))
    print(classify_triangle(4,2,3))
    unittest.main()

