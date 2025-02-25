# for overriding:
#   should inherit
#   should have same function name

class Parent:
    def gift(self):
        print("basic laptop")

class Child(Parent):
    def gift(self):
        print("macbook pro")

obj = Child()
obj.gift()

# overloading is not possible in python
# class MyClass:
#     def add(self, a):
#         print(a)
#     def add(self, a, b):
#         print(a + b)
#     def add(self, a, b, c):
#         print(a + b + c)

# obj = MyClass()
# obj.add(1)
# only remembers the last written function i.e. add(self, a, b, c)