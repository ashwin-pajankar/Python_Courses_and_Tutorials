class Person:

    def method1(self, a, b, c):
        self.var1 = a
        self.var2 = b
        self.var3 = c

class Employee(Person):
    pass

obj1 = Person()
obj2 = Employee()

obj1.method1(1, 2, 3)
print(obj1.var1, obj1.var2, obj1.var3)

obj2.method1(3, 1, 2)
print(obj2.var1, obj2.var2, obj2.var3)
