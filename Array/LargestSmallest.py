#Smallest and Largest Element in an array using Python

arr = [10, 89, 9, 56, 4, 80, 8]
mini =  arr[0]
maxi = arr[0]

for i in range(len(arr)):
    if arr[i] < mini:
        mini = arr[i]
    if arr[i] > maxi:
        maxi =  arr[i]
print(f'mininum is : {mini} \n maximum is : {maxi}')

#Method2
arr = [10, 89, 9, 56, 4, 80, 8]
arr.sort()
print(arr[0])
print(arr[-1])

#Method3
arr = [10, 89, 9, 56, 4, 80, 8]

print (min(arr))
print (max(arr))