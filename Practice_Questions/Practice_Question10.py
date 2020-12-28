# 10)	Python Program to get Current Date and Time using Python.


from datetime import datetime
now = datetime.now()
current_date = now.strftime("%d/%m/%Y")
current_time = now.strftime("%H:%M:%S")
print("\nCurrent Date is =", current_date)
print("Current Time is =", current_time, '\n')




# import time
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S", t)
# print(current_time)
