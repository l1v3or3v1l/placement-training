class Parent:
    def info(self):
        print("I am Parent")
    def add(self, a, b):
        print(a + b)

class Child1(Parent):
    def detail(self):
        print("I am Child 1")
    def mul(self, a, b):
        print(a * b)

class Child2(Parent):
    def name(self):
        print("I am Child 2")
    def sub(self, a, b):
        print(a - b)

obj1 = Child1()
obj1.info()
obj1.add(5, 4)
obj1.detail()
obj1.mul(5, 2)
obj2 = Child2()
obj2.info()
obj1.add(5, 6)
obj2.name()
obj2.sub(5, 2)
