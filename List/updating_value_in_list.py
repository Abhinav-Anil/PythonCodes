#Program to illustrate updating values in a list

num_list = [1,2,3,4,5,6,7,8,10]
print("List is :", num_list)
num_list[5] = 100
print("List after updation is :", num_list)
num_list.append(200)
print("List after appending value is :", num_list)
del num_list[3]
print("List after deleting a value is :", num_list)