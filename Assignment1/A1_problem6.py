# Convert the following into dictionary without using any inbuilt functions.
# keys = ['Ten','Twenty','Thirty']
# values = [10,20,30]




keys = ['Ten','Twenty','Thirty']
values = [10,20,30]
dic = {}

for i in range(len(keys)):
    dic[keys[i]] = values[i]

print("The keys in the dictionary are : ",keys)
print("The values in the dictionary are : ",values)
print("The output dictionary is : ",dic)


