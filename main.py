# This entrypoint file to be used in development. Start by reading README.md
import shape_calculator
from unittest import main

"""
rect = shape_calculator.Rectangle(5, 10)
print(rect.get_area())
rect.set_width(3)
print(rect.get_perimeter())
print(rect)
"""


print("Square_Tests")
sq = shape_calculator.Square(9)

#print(sq.get_area())
sq.set_side(4)
#print(sq.get_diagonal())
print(sq)

print("Test_Set_Sq:")
print(sq)
sq.set_height(3)
print("set height 3: ", sq)
sq.set_width(6)
print("set width 6: ", sq)

# Run unit tests automatically
#main(module='test_module', exit=False)