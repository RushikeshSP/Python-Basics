# 5. Practice of Inheritance

# Inheritance
# Types of Inheritance
# 1. Simle Inheritance
# 2. Mupltiple Inheritance
# 3. Multi-level Inheritance
# 4. Hierarchical Inheritance
# 5. Hybrid Inheritance


'''
# 1. Simple Inheritance
class parent():
    p = "Parent class variable"
    def p1(self):
        print("In p1 function of parent class")
    def p2(self):
        print("In p2 function of parent class")

class child(parent):
    c = "child class variable"
    def c1(self):
        print("In c1 function of child class")
    def c2(self):
        print("In c2 function of child class")

obj = child()
print(obj.c)
obj.c1()
obj.c2()
print(obj.p)
obj.p1()
obj.p2()
'''


'''
# 2. Multiple Inheritance
class parent1():
    p1 = "Parent1 class variable"
    def fun1(self):
        print("In fun1 function of parent1 class")
    def fun2(self):
        print("In fun2 function of parent1 class")
class parent2():
    p2 = "Parent2 class variable"
    def func1(self):
        print("In fun1 function of parent2 class")
    def func2(self):
        print("In fun2 function of parent2 class")

class child(parent1, parent2):
    c = "child class variable"
    def c1(self):
        print("In c1 function of child class")
    def c2(self):
        print("In c2 function of child class")

obj = child()
print(obj.c)
obj.c1()
obj.c2()
print(obj.p1)
obj.fun1()
obj.fun2()
print(obj.p2)
obj.func1()
obj.func2()
'''


'''
# 3. Multi-level Inheritance
class first():
    def f1(self):
        print("In first class")
class second(first):
    def f2(self):
        print("In second class")
class third(second):
    def f3(self):
        print("In third class")

obj = third()
obj.f1()
obj.f2()
obj.f3()
'''


'''
# 4. Hierarchical Inheritance
class parent():
    p = "Parent class variable"
    def p1(self):
        print("In p1 function of parent class")
    def p2(self):
        print("In p2 function of parent class")

class child1(parent):
    c1 = "child class1 variable"
    def f1(self):
        print("In f1 function of child class1")
    def f2(self):
        print("In f2 function of child class1")
class child2(parent):
    c2 = "child class2 variable"
    def fun1(self):
        print("In fun1 function of child class2")
    def fun2(self):
        print("In fun2 function of child class2")

obj1 = child1()
print(obj1.c1)
print(obj1.p)
obj1.f1()
obj1.f2()
obj1.p1()
obj1.p2()
obj2 = child2()
print(obj2.c2)
print(obj2.p)
obj2.fun1()
obj2.fun2()
obj2.p1()
obj2.p2()
'''



# 5. Hybrid Inheritance
class parent():
    p = "Parent class variable"
    def p1(self):
        print("In p1 function of parent class")
    def p2(self):
        print("In p2 function of parent class")

class child1(parent):
    c1 = "child class1 variable"
    def f1(self):
        print("In f1 function of child class1")
    def f2(self):
        print("In f2 function of child class1")
class child2(child1,parent):
    c2 = "child class2 variable"
    def fun1(self):
        print("In fun1 function of child class2")
    def fun2(self):
        print("In fun2 function of child class2")

obj1 = child1()
print(obj1.c1)
print(obj1.p)
obj1.f1()
obj1.f2()
obj1.p1()
obj1.p2()
obj2 = child2()
print(obj2.c2)
print(obj2.p)
obj2.fun1()
obj2.fun2()
obj2.p1()
obj2.p2()
obj2.f1()

