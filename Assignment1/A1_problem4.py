'''
Print the following....
if n = 5
*
**
***
****
*****
'''

# n = int(input('Enter a number to get pattern of * :' ))
# k = 1
# for i in range(n):
#     for j in range(k):
#         print("*", end=' ')
#     k = k+1
#     print("")

n=int(input('Enter a number to get pattern of * :'))
for i in range(1,n+1): 
    print('* ' * i)