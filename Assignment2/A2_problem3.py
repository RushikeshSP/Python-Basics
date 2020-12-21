# 3. Practice of classes and objects.


# Que- Program for simple calculator using class
class simple_calculator():
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def div(self,a,b):
        return a/b
    def multi(self,a,b):
        return a*b

print("Enter your choice : ")
print("1. For addition ")
print("2. For subtraction ")
print("3. For multiplication ")
print("4. For division ")
c = int(input("choice = "))
obj = simple_calculator()
if(c==1):
    n1 = int(input("Enter First number : "))
    n2 = int(input("Enter second number : "))
    print(f"The addition of {n1} and {n2} is : ", obj.add(n1,n2))
elif(c==2):
    n1 = int(input("Enter First number : "))
    n2 = int(input("Enter second number : "))
    print(f"The subtraction of {n1} and {n2} is : ", obj.sub(n1,n2))
elif(c==3):
    n1 = int(input("Enter First number : "))
    n2 = int(input("Enter second number : "))
    print(f"The multiplication of {n1} and {n2} is : ", obj.multi(n1,n2))
elif(c==4):
    n1 = int(input("Enter First number : "))
    n2 = int(input("Enter second number : "))
    print(f"The division of {n1} and {n2} is : ", obj.div(n1,n2))
else:
    print("invalide choice.")