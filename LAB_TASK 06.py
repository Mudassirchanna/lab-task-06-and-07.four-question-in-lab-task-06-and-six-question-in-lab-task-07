# LAB_TASK 06
"""Q;NO:03 data ={'a':1, 'b':2, 'c':3} create a dictionary where the 
original values becomes keys and keys becomes values.
output:{1:'a', 2:'b', 3:'c'}"""

data = {'a':1, 'b':2, 'c':3}
reverse={}
for key in data :
    value=data[key]
    reverse[value]=key
    print(reverse)