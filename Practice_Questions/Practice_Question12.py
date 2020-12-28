# 12)	Python Program to for Print Number series without using any loop.



'''
N = int(input("Enter the number up which you want to print number series : "))
def NumSeries(num):
    if(num>0):
        NumSeries(num-1)
        print(num)

NumSeries(N)
'''



N = int(input("Enter the number up which you want to print number series : "))
temp = 1

def NumSeries(temp,num):
    if (num>0):
        print(temp)
        temp +=1
        NumSeries(temp,num-1)

NumSeries(temp,N)

