import sys
age = input("Enter your age: ")
if int(age) < 18:
    sys.exit("Age less than 18")
else:
    print("Age is not less than 18")