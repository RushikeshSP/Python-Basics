# 8)	Python Program to find most common element in a 2D list.
# Input : [[10, 20, 30], [20, 50, 10], [30, 50, 10]]
# Output : 10



list_2D = []

print("Enter the dimensions of list : ")
m = int(input("Enter the value of Row : "))
n = int(input("Enter the value of Column : "))

for i in range(m):
    list1 = []
    for j in range(n):
        ele = int(input("Enter a Element : "))
        list1.append(ele)
    list_2D.append(list1)

# print(list_2D)

def MostCommonElement(list_2D):
    temp_lis = [j for i in list_2D for j in i]
    mos_com_ele = max(temp_lis, key= temp_lis.count)
    return mos_com_ele

print("The most common element in a given 2D list is : ",MostCommonElement(list_2D))