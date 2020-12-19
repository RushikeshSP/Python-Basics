# Write a python program to find the list of words that are longer than n from a given list of words.Take input from user.
# Take n = 9.

list = []
Result = []
a = int(input("Enter the number of words you want in given list : "))
print("Enter the words : ")
for i in range(a):
    w = input(f"word {i+1} : ")
    list.append(w)

print("Input List : ",list)
 
for i in list:
    if(len(i)>9):
        Result.append(i)

print("Result : ",Result)

# for i in list:
#     if(len(i)>9):
#         print(i,end=" ")

