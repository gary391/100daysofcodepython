"""
class inheretance

inherit appearance
inherit skills or behavior
"""
class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale")


class Fish(Animal): # Inhertance

    def __init__(self):
        super().__init__()

    def swin(self):
        print("moving in water.")
    # def __init__(self):
    #     super().__init__() # refer to the super class that is being inhereted from

    def breathe(self):
        super().breathe()
        print("breathe inside the water")
nemo = Fish()
nemo.swin()
nemo.breathe()
print(nemo.num_eyes)

