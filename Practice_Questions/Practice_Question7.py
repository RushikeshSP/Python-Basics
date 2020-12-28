# 7)	Python Program to remove all duplicate occurring tuple records.

# The original list : [(3, 4), (4, 5), (3, 4), (3, 6), (4, 5), (6, 7)]
# All the non Duplicate from list are : [(6, 7), (3, 6)]

# Constant input
lis = [(3, 4), (4, 5), (3, 4), (3, 6), (4, 5), (6, 7)]

freq = []
Non_Duplicate = []

for i in range(len(lis)):
    count = 0
    for j in range(len(lis)):
        if(lis[i] == lis[j]):
            count +=1
    freq.append(count)

for i in range(len(freq)):
    if(freq[i] == 1):
        Non_Duplicate.append(lis[i])


print("The original Input List is : ",lis)
print("The list without Duplicate Occuring Tuple Records is : ",Non_Duplicate)
    





