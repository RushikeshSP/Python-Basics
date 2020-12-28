# 5)	Python Program to perform Bubble Sort.



N = int(input("Enter how many elements do you want in list : "))
lis = [int(input("Enter a number : ")) for i in range(N)]
print("User Entered list is : ",lis)

def BubbleSort():
	for i in range(len(lis)-1):
		for j in range(len(lis)-1-i):
			if(lis[j]>lis[j+1]):
				lis[j], lis[j+1] = lis[j+1], lis[j]

BubbleSort()
print("Sorted list using Bubble Sort is : ",lis)


