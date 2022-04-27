#Sort First half in Ascending and Second half in descending order

#Method1
def printOrder(arr, n):
    arr.sort()

    i = 0
    while (i < n/2):
        print(arr[i])
        i += 1
    
    j = n -1 
    while j >= n/2:
        print(arr[j])
        j = j-1

arr = [5, 4, 6, 2, 1, 3, 8, 9, 7]
n = len(arr)

printOrder(arr, n)
