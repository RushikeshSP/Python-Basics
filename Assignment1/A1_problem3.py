# Check if all items in the tuple are the same and print "True" else print "False".
# (2,2,2,2,2,2,2) = True
# (2,2,2,3,4,4,4) = False

tup1 = (2,2,2,2,2,2,2,2,2,2)
tup2 = (2,2,2,3,3,3,4,4,2,2)

# For tuple 1
print(tup1)
temp = 1
for i in range(len(tup1)-1):
    if(tup1[i]!=tup1[i+1]):
        temp = 0 
        break
if (temp == 1):
    print("True")
else:
    print("False")


# For tuple 2
print(tup2)
temp = 1
for i in range(len(tup2)-1):
    if(tup2[i]!=tup2[i+1]):
        temp = 0 
        break
if (temp == 1):
    print("True")
else:
    print("False")


