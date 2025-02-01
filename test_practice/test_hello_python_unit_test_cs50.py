from hello_python_unit_test_cs50 import hello


def test_default(): 
  
    assert hello() == "hello, world"
    
def test_argument():
    for name in ["David", "Harry", "marry"]:
        assert hello(name) == f"hello, {name}" ## Here we are validating the return value 
    ## which is not valid test case here as we are printing the value and not returning anything.