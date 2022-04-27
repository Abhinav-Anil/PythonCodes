#Find the Sum of the Numbers in a Given Interval 

'''
Given two integer inputs as the range [low , high], 
the objective is to find the sum of all the numbers that lay in the given integer inputs as interval. 
In order to do so we usually iterate through the the numbers in the given range and keep appending 
them to the sum variable. Here are few methods to solve the above mentioned problem in Python Language.

Method 1: Using Brute Force
Method 2: Using the Formula
Method 3: Using Recursion
'''

#Method1

num1, num2 = 3,6
total = 0

for i in range(num1, num2+1):
    total = total + i
print(total)

#Method2
num1, num2 = 3,6

total = num2*(num2 + 1)/2 - num1*(num1 + 1)/2 + num1
print(total)

#Method3
def getSum(total, num1, num2):
    if num1 > num2:
        return total
    return num1 + getSum(total, num1+1, num2)

num1, num2 = 3,6
total = 0

print(getSum(total, num1, num2))
