# 2. Practice of Functions (filter() Function, map() Function, reduce() Function, lambda Functions).


'''
# Que- Program for simple calculator using Functions
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def div(a,b):
    return a/b
def multi(a,b):
    return a*b

print("Enter your choice : ")
print("1. For addition ")
print("2. For subtraction ")
print("3. For multiplication ")
print("4. For division ")
c = int(input("choice = "))
if(c==1):
    n1 = int(input("Enter First number : "))
    n2 = int(input("Enter second number : "))
    print(f"The addition of {n1} and {n2} is : ", add(n1,n2))
elif(c==2):
    n1 = int(input("Enter First number : "))
    n2 = int(input("Enter second number : "))
    print(f"The subtraction of {n1} and {n2} is : ", sub(n1,n2))
elif(c==3):
    n1 = int(input("Enter First number : "))
    n2 = int(input("Enter second number : "))
    print(f"The multiplication of {n1} and {n2} is : ", multi(n1,n2))
elif(c==4):
    n1 = int(input("Enter First number : "))
    n2 = int(input("Enter second number : "))
    print(f"The division of {n1} and {n2} is : ", div(n1,n2))
else:
    print("invalide choice.")
'''

'''
# filter() Function
string = input("Enter a string : ")
def check_vowels(s):
    vowels = "aeiouAEIOU"
    print(s)
    if(s in vowels):
        return True
    else:
        return False
result = list(filter(check_vowels, string))
t = set(result)
print("The vowels present in given string are : ", *t)
'''

'''
# map() and lambda Functions
l1 = [11,10,3,2,5,6,9]
l2 = [3,5,8,0,2,5,8]
add_list_ele = map(lambda n1,n2: n1+n2, l1,l2)
print("List1: ",l1)
print("List2: ",l2)
print("Addition of list1_elements and list2_elements is : ",list(add_list_ele))
'''


# Reduce() Function
from functools import reduce
def multi(x,y):
    # print("x= ",x , " y= ",y)
    return x*y
n = int(input("Enter a number to find Factorial : "))
fact = reduce(multi, range(1,n+1))
print(f"Factorial of {n} is : ", fact)






