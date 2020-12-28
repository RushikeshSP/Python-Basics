# 2. Python Program for Sum of squares of first n natural numbers.
# Given a positive integer N. The task is to find 1^2+2^2+3^2+..+n^2.


N = int(input("Enter a Positive Integer Number : "))

sum = 0

for i in range(1,N+1):
    sum = sum + (i**2)

print(f"The sum of squares of first {N} natural numbers is : ", sum)