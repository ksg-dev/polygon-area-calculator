# This entrypoint file to be used in development. Start by reading README.md
import shape_calculator
from unittest import main

"""
rect = shape_calculator.Rectangle(5, 10)
print(rect.get_area())
#rect.set_width(3)
#print(rect.get_perimeter())
print(rect)
rect.set_width(7)
rect.set_height(3)
print(rect)
testr = rect.get_picture()
print(testr)



print("Square Section")

sq = shape_calculator.Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
sq.set_side(2)
print(sq)
testsq = sq.get_picture()
print(testsq)
"""

print("Get Amount Inside:")
rect = shape_calculator.Rectangle(3,6)
sq = shape_calculator.Square(5)


rect.set_height(10)
rect.set_width(15)
#print(rect.get_picture())
get_am = rect.get_amount_inside(sq)
print("6: ", get_am)

rect2 = shape_calculator.Rectangle(4, 8)
actual = rect2.get_amount_inside(rect)
print("1: ", actual)

rect3 = shape_calculator.Rectangle(2, 3)
actual3 = rect3.get_amount_inside(rect)
print("0: ", actual3)


# Run unit tests automatically
main(module='test_module', exit=False)