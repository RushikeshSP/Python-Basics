# 9)	Python Program to convert time from 12 hour to 24-hour format.

  

def convert24(str1): 
      
    if str1[-2:] == ("AM" or "am") and str1[:2] == "12": 
        return "00" + str1[2:-2] 
          
    # remove the AM     
    elif str1[-2:] == ("AM" or "am"): 
        return str1[:-2] 
         
    elif str1[-2:] == ("PM" or "pm") and str1[:2] == "12": 
        return str1[:-2] 
          
    else: 
          
        # add 12 to hours and remove PM 
        return str(int(str1[:2]) + 12) + str1[2:8] 
  

time = input("Enter time in format HH:MM:SS AM/PM   : ")
# print(convert24("08:05:45 PM")) 
print("Given time in 24 hr format is : ",convert24(time)) 










