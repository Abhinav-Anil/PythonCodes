#Sum of all the elements of an array

#Method1
arr = [12, 13, 1, 10, 34, 10]
sum = 0

for i in range(len(arr)):
    sum = sum  + arr[i]
print(sum)

#Method2
def getSum(arr, index):
    if index == len(arr -1):
        return arr[index]
    return arr[index] + getSum(arr, index+1)