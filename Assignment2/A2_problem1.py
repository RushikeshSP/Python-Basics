# 1. practice of list comprehensions and dictionary comprehensions.


# Que- Find Transpose of a matrix.
# Transpose using Nested Loops
Transpose = []
Matrix = [[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(Matrix)):
    Transpose_row = []
    for row in Matrix:
        Transpose_row.append(row[i])
    Transpose.append(Transpose_row)
print(Transpose)

# Ṭranspose using list comprehensions
Matrix = [[1,2,3],[4,5,6],[7,8,9]]
Transpose = [[row[i] for row in Matrix] for i in range(len(Matrix)) ]
print(Transpose)




# Que- print number: (number)^2 in output using dictionary within given range.
# Using loops
sq_dict = dict()
n = int(input("Enter the range : "))
for i in range(n+1):
    sq_dict[i]=i*i
print(sq_dict)

# Using dictionary comprehensions
n = int(input("Enter the range : "))
sq_dict = {i:i*i for i in range(n+1)}
print(sq_dict)