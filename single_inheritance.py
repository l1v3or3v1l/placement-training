class Parent:
    def info(self):
        print("I am Parent")
    def add(self, a, b):
        print(a + b)

class Child(Parent):
    def name(self):
        print("I am Child")
    def sub(self, a, b):
        print(a - b)

obj = Child()
obj.info()
obj.add(5, 4)
obj.name()
obj.sub(5, 2)