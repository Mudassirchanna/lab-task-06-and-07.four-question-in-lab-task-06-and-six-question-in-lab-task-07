# LAB_TASK 07
"""Q:NO:04 ask the user for a number and check wether 
it exists in the set {10,20,30,40,50}."""

numbers = {10,20,30,40,50}
num = int(input("enter a numbers : "))
if num in numbers:
    print("number exists in the set ")
else:
    print("number does not exists in the set")
