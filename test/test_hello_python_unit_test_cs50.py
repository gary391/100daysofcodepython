from hello_python_unit_test_cs50 import hello

def test_default():
    assert hello() == "hello, world"
    
def test_argument():
    assert hello("David") == "hello, David"