# 11)	Python Program to perform Merge Sort. (Look up the logic behind Merge Sort.)


def mergeSort(list1):
    if (len(list1)>1):
        mid = len(list1)//2
        left_list = list1[:mid]
        right_list = list1[mid:]
        mergeSort(left_list)   
        mergeSort(right_list)

        i = j = k = 0
        while(i<len(left_list) and j<len(right_list)):
            if(left_list[i]<right_list[j]):
                list1[k]=left_list[i]
                i+=1
                k+=1
            else:
                list1[k]=right_list[j] 
                j+=1
                k+=1
        while(i<len(left_list)):
            list1[k]=left_list[i]
            i+=1
            k+=1
        while(j<len(right_list)):
            list1[k]=right_list[j]
            j+=1
            k+=1


N = int (input("Enter how many numbers do you want in list : "))
list1 = [int(input("Enter a number : ")) for i in range(N)]
print("User Entered list is : ",list1)
mergeSort(list1)
print("Sorted list using merge sort is : ",list1)