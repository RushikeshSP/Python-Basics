'''
Print the following....
if n = 5
1
12
123
1234
12345
'''

n = int(input("Enter number : " ))
for i in range(n):
    for j in range(i+1):
        print(j+1,end=' ')
    print()


# n= int(input("Enter number:"))
# list3= [ ]
# for i in range(1, n+1 ):
#     if i!=0 :
#         list3.append(i)
#         print(*list3)