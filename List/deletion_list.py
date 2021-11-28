#Program to illustrate deletion of numbers from a list using del statements
'''
use del method when exactly know which elements to delete, otherwise use the remove() method to delete the unkown elements"
'''

num_list = [1,2,3,4,5,6,7,8,10]
del num_list[2:4] #deletes numbers at index 2 and 3
print("num list after deleting at fix index :", num_list)

del num_list[:] #deletes all the elements from the list
print("After deleting all the elements from the list :", num_list)