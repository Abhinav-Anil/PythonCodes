#Check if a Number is Positive and Negative in Python

'''
Given an integer input, the objective is check whether the given integer is Positive or Negative. In order to do so we have the following methods,

Method 1: Using Brute Force
Method 2: Using Nested if-else Statements
Method 3: Using ternary operator

'''

#Method 1
num = 15
if num==0:
    print("Zero")
elif num>0:
    print('postive')
else:
    print('Negative')

#Method 2
num = 15
if num >= 0:
    if num == 0:
        print('Zero')
    else:
        print('Postive')
else:
    print('Negative')

#Method3
num = 15
print('Postive' if num>=0 else 'Negative')