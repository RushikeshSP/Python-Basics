# 4)	Python Program to perform Binary Search.


N = int(input("Enter how many elements do you want in list : "))
lis = [int(input("Enter number : ")) for i in range(N)]
lis.sort()
print("Input list is : ",lis)
key = int(input("Enter the key number which you want to search : "))

def BinarySearch(lis,key):
    low = 0
    high = len(lis)-1
    flag = False
    while(low<=high):
        mid = (low+high)//2
        if(key == lis[mid]):
            flag = True
            break
        elif(key>lis[mid]):
            low = mid+1
        else:
            high = mid-1
    if(flag == True):
        print(f"The key number {key} is found.")
    else:
        print(f"The key number {key} is not found.")

BinarySearch(lis,key)
