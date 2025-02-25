class Mother:
    def detail(self):
        print("I am Mother")
    def mul(self, a, b):
        print(a * b)

class Father:
    def info(self):
        print("I am Father")
    def add(self, a, b):
        print(a + b)

class Child(Mother, Father):
    def name(self):
        print("I am Child")
    def sub(self, a, b):
        print(a - b)

obj = Child()
obj.detail()
obj.mul(5, 2)
obj.info()
obj.add(5, 4)
obj.name()
obj.sub(5, 2)
