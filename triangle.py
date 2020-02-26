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


def classify_triangle(side_a, side_b, side_c):
    """A function that can classify the type of one triangle with three numbers."""

    # To make sure these three numbers can make up a triangle.
    if side_a + side_b > side_c and side_b + side_c > side_a and side_a + side_c > side_b:
        n_list = list()
        n_list.append(side_a)
        n_list.append(side_b)
        n_list.append(side_c)
        new_list = sorted(n_list)
        if new_list[0] * new_list[0] + new_list[1] * new_list[1] == new_list[2] * new_list[2]:
            result = "Right triangle."

        if side_a == side_b == side_c:
            result = "Equilateral triangle."

        if side_a == side_b or side_a == side_c or side_b == side_c:
            result = "Isosceles triangle."

        if side_a != side_b != side_c:
            result = "Scalene triangle."

    else:
        result = "Not a triangle."

    return result


class TextFunction(unittest.TestCase):
    """Unit Test"""

    def test_classify_triangle(self):
        """unit test to check classify triangle function"""
        self.assertTrue(classify_triangle(5, 4, 3), "5, 4, 3 can make up Right triangle.")
        self.assertTrue(classify_triangle(1, 1, 1), "1, 1, 1 can up Equilateral triangle.")
        self.assertTrue(classify_triangle(1, 2, 3), "1, 2, 3 Can Not make up the triangle.")
        self.assertTrue(classify_triangle(6, 6, 10), "6, 6, 10 can make up Isosceles triangle.")
        self.assertTrue(classify_triangle(4, 2, 3), "4, 2, 3 can make up Scalene triangle.")


if __name__ == "__main__":
    print(classify_triangle(5, 4, 3))
    print(classify_triangle(1, 1, 1))
    print(classify_triangle(1, 2, 3))
    print(classify_triangle(6, 6, 10))
    print(classify_triangle(4, 2, 3))
    unittest.main()
