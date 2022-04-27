'''
/*
 * @author Abhinav Anil
 * @email abhinav.anil2206@gmail.com
 */
'''


'''
Check Whether a Number is Even or Odd in Python
Given an integer input the objective is to write a Python code to Check Whether a Number is Even or Odd. 
To do so the main idea is to divide the number by 2 and check if it’s divisible or not. 
It’s an Even number is it’s perfectly divisible by 2 or an Odd number otherwise.

Here are the Methods to solve the above mentioned problem,
Method 1 : Using Brute Force
Method 2 : Using Ternary Operator
Method 3 : Using Bitwise Operators
'''

#Method1

user_input = int(input('Enter the number: '))

if user_input % 2 == 0:
    print('Number is even')
else:
    print('Number is odd')

#Method2

user_input = int(input("Enter the number: "))
print('even' if user_input % 2 == 0 else 'odd')

#Method3
user_input = int(input("Enter the number: "))

def isEven(user_input):
    return not user_input&1

if __name__ == "__main__":
  if isEven(user_input):
    print('Even')
  else:
    print('Odd')
