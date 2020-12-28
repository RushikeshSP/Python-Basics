# 3)	Python program to find Cumulative sum of a list.
# Input : list = [10, 20, 30, 40, 50]
# Output : [10, 30, 60, 100, 150]

n= int(input("Enter how many numbers do you want in the list : "))
lis = []
for i in range(n):
    num = int(input("Enter the number : "))
    lis.append(num)
print("User Entered List is : ",lis)

for i in range(n-1):
    lis[i+1]= lis[i]+lis[i+1]
print("The Cumulative Sum of the list is : ",lis)


