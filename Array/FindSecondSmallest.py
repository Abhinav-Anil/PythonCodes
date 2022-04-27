#Second Smallest Element in an array using Python

#Method1 
import math

arr = [10, 13, 17, 11, 34, 21]
first = second = math.inf

for i in range(0, len(arr)):
   if arr[i] < first:
     first = arr[i]

for i in range(0, len(arr)):
   if arr[i] != first and arr[i] < second:
       second = arr[i]

print(second)

#Method2
import math

arr = [10, 13, 17, 11, 34, 21]
first = second = math.inf

for i in range(0, len(arr)):
    if first > arr[i]:
        second = first
        first = arr[i]
    else:
        if arr[i] != first and arr[i] <second:
            second =  arr[i]
print(second)


#Method3
arr = [10, 13, 17, 11, 34, 21]
arr.sort()
print(arr[1])