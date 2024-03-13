'''
Modify the add function to take an unlimited number of arguments.
Use a loop to sum all the arguments inside the function.
Test it out by calling add() to calculate sum of some arguments.
'''


# *args is a tuple which is being passed to the function
# Using the * allows packing all the numbers into a tuple.
# Which is then passed to the function.
def add(*args):
    sum = 0
    for n in args:
        sum = sum + n
    return sum


print(add(1, 2, 3, 4, 5, 6, 6, 67, ))


def calculate(n, **kwargs):
    print(type(kwargs))
    # for k,v in kwargs.items():
    #     print(k,v)
    print(kwargs["add"])
    n = n + kwargs['add']
    n = n * kwargs['multiply']
    print(n)


calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        self.make = kw['make']
        self.model = kw.get('model')
        self.color = kw.get('color')
        self.seats = kw.get('seats')


my_car = Car(make="Nissan", model="GTR", color="Black", seats="Two")
print(my_car.model)
