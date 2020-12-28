# 1)	Python Program to check Armstrong Number.
# Given a number x, determine whether the given number is Armstrong number or not. A positive integer of n digits is called an Armstrong number of order n (order is number of digits) if-
# abcd... = pow(a,n) + pow(b,n) + pow(c,n) + pow(d,n) + ....
# Input : 153
# Output : Yes
# 153 is an Armstrong number.
# 1*1*1 + 5*5*5 + 3*3*3 = 153

Num = int(input("Enter a number : "))
Temp = Num
l_digit = 0
Result = 0
while(Temp>0):
    l_digit = Temp%10
    Result = Result+(l_digit**3)
    Temp = Temp//10

if(Num == Result):
    print(f"{Num} is an Armstrong Number.")
else:
    print(f"{Num} is Not an Armstrong Number.")

    
