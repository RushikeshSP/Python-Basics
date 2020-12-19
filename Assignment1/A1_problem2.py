# Wrire a python program to convert a tuple of string values to a tuple of integer values.

tup = ("1","22","333","4444","55555")         #Taking a constant string input.
Result = []
print("Input String Tuple : ",tup)

# for i in tup:     
#     Result.append(int(i))  
Result = [int(i) for i in tup]                  

print("Output Integer Tuple : ",tuple(Result))

    


