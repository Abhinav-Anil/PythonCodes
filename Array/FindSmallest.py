#Find smallest element in an array using Python

#Method1

arr = [10,89,9,56,4,80,8]
mini = arr[0]

for i in range(len(arr)):
    if arr[i] < mini:
        mini = arr[i]
print(mini)

#Method2
arr = [10,89,9,56,4,80,8]
arr.sort()
print(arr[0])

#Method3
arr = [10,89,9,56,4,80,8]
print(min(arr))