class BaseClass:
    def add(self, a, b):
        c = a + b
        print("Addition is : ", c)

class DerivedClass(BaseClass):
    def mul(self, a, b):
        c = a * b
        print("Multiplication is : ", c)

class OverClass(DerivedClass):
    def add(self, *args):
        c = sum(args)
        print("Addition is : ", c)

    def mul(self, *args):
        c = 1
        for num in args:
            c *= num
        print("Multiplication is : ", c)

# Testing the classes
obj = DerivedClass()
obj.add(10, 20)
obj.mul(10, 20)
print("---------------------------------")
obj2 = OverClass()
obj2.add(10, 20, 30)  # Overloaded Function
obj2.mul(2, 4, 6)     # Overloaded Function