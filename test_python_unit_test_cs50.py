from python_unit_test_cs50 import square
import pytest


# def main():
#     test_square()

# This is a convention to append a test infront of function name.
# Also we need to run this function as well to test the test cases.

# def test_square():
#     if square (2) != 4:
#         print("2 square was not 4")
#     if square (3) !=9:
#         print("3 square was not 9")

### Using assert key word
# def test_square():
#     try:
#         assert square(2) == 4
#     except AssertionError:
#         print("2 square was not 4")
#     try:
#         assert square(3) == 9
#     except AssertionError:
#         print("3 square was not 9")
#     try:
#         assert square(-2) == 4
#     except AssertionError:
#         print("-2 square was not 4")
#     try:
#         assert square(-3) == 9
#     except AssertionError:
#         print("-3 square was not 9")
#     try:
#         assert square(0) == 0
#     except AssertionError:
#         print("0 square was not 0")

### Using the pytest
# def test_square():
#     assert square(2) == 4
#     assert square(3) == 9 
#     assert square(-2) == 4
#     assert square(-3) == 9
#     assert square(0) == 0

## Splitting the tests separately can also help in identifying the problem.

def test_positive ():
    assert square (2) == 4
    assert square (3) == 9

def test_negative ():
    assert square (-2) == 4
    assert square (-3) == 9

def test_zero():
    assert square(0) == 0
    
def test_str():
    with pytest.raises(TypeError):
        square('cat')


# if __name__ == "__main__":
#     main()