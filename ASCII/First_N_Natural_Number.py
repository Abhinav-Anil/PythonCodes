#Find the Sum of the First N Natural Numbers in Python

'''
Given an integer input of N, the objective is to find the sum of all the natural numbers until the given input integer. 
To do so we can use different approaches to write the Python code and some such methods are mentioned below,

Method 1 : Using for Loop
Method 2 : Using Formula for the Sum of Nth Term
Method 3 : Using Recursion

'''

#Method1
total = 0
num = 2

for i in range(num+1):
    total += i
print(total)

#Method2
num = 10
total = num*(num + 1)/2
print(total)

#Method3
num = 5

def getSum(num):
    if num == 1:
        return 1
    else:
        return num +getSum(num - 1)

print(getSum(num))