# 14)	Python Program to Count Uppercase, Lowercase, special character and numeric values using Regex. (Read up on Regex before solving this.)


import re 
  
  
string = input("Enter a string : ")
  
# Creating separate lists using  
# the re.findall() method. 
uppercase_characters = re.findall(r"[A-Z]", string) 
lowercase_characters = re.findall(r"[a-z]", string) 
special_characters = re.findall(r"[, .!?]", string) 
numerical_characters = re.findall(r"[0-9]", string) 
  
print("The no. of uppercase characters in given string are : ", len(uppercase_characters)) 
print("The no. of lowercase characters in given string are : ", len(lowercase_characters)) 
print("The no. of special characters in given string are : ", len(special_characters)) 
print("The no. of numerical characters in given string are : ", len(numerical_characters)) 

