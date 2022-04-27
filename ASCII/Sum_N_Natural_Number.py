#Find the Sum of N Natural Numbers
'''
Given an integer value the objective of the code is to sum up all the numbers until the input integer number. 
To do so we usually use iteration, we iterate through the numbers until the input number is reached 
while appending the number to the sum variable. Here are some methods to solve the above mentioned problem

Method 1: Using for Loop
Method 2: Using Formula
Method 3: Using Recursion

'''

#Method1
num = 6
total = 0

for i in range(num+1):
    total = total + i
print(total) 

#Method2
num = 6
total = num*(num + 1 )/2
print(total)

#Method3
def getSum(num):
    if num == 0 :
        return num
    else:
        return num + getSum(num -1)

print(getSum(6))



