# 4. Practice of Constructors and Distructors


'''
# Constructors
class Student:
    college = "AVCOE"
    def __init__(self, name, id, roll_no):
        self.name = name
        self.id = id
        self.roll_no = roll_no

    def display(self):
        print("College Name : ",Student.college)
        # print(self.college)
        print("Student Name : ",self.name)
        print("Student Id : ",self.id)
        print("Student Roll_no : ",self.roll_no)

s1 = Student("Rushikesh",111,2227)
s1.display()
print(" ")
s2 = Student("Aditya",112,2268)
s2.display()
'''

# Distructors
class Temp():
    print("In class")
    def __init__(self):
        print("In init mathod(Constructor)")
    def __del__(self):
        print("In del method(Distructor)")
    def display(self):
        print("In display method")

T1 = Temp()
T1.display()
T2 = Temp()
T2.display()
T3 = Temp()
del T3







