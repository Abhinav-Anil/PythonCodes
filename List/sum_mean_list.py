#Program to find the sum and mean of elemetns in a list

num_list = [1,2,3,4,5,6,7,8,9,10]

sum_list = 0

for i in num_list:
    sum_list += i
    average  = sum_list/float(len(num_list))
print('Sum of elements in a list :', sum_list)
print('Average of elements in a list :', average)