# TASK 2
# Create a function that takes a list of integers and returns what the
# smallest number is in
# Do not use built in function
# eg for the list [42,13,56,7,12,3,85] the function should return 5,
# because the smallest is found at the index in this list.

my_list = [42, 13, 56, 7, 12, 3, 85]
item = 3

def my_min(my_list):
    low = 0
    for element in my_list:
        if element < low:
            low = element
    return low
print(min(my_list))
index = my_list.index(item)

print('The index of', item, 'in the list is:', index)
