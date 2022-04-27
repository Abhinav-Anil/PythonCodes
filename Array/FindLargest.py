#Largest Element in an array using python
#Method1

arr = [10, 8, 90, 34, 56, 78]
arr.sort(reverse = True)
print(arr[0])

#Method2
arr = [10, 8, 90, 34, 56, 78]
print(max(arr))

#Method3
arr = [10, 8, 90, 34, 56, 78]
max_element =  arr[0]

for i in range(len(arr)):
    if arr[i] > max_element:
        max_element =  arr[i]

print(max_element)