# 6)	Python Program to find the most occurring character in a String and also display its count.
# Input : hello
# Output : ('l', 2)



string = input("Enter a string : ")
# string = string.lower()
freq = []
for i in range(len(string)):
    count = 1
    for j in range(i+1,len(string)):
        if (string[i] == string[j]):
            count +=1 
    freq.append(count)
# print(freq)
max_freq = max(freq)
# print(max_freq)

index = []
for i in range(len(freq)):
    if(freq[i]==max_freq):
        index.append(i)

print(f"Most occuring character is",end=" ")
for i in index:
    print(f"'{string[i]}'",end=" ")

print(f"and its count is '{max_freq}'.")



    