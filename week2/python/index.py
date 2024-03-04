# CREATE AN EMPTY ARRAY
my_list = []

# APPEND 10,20,30,40
my_list.append(10)
my_list.extend([20,30,40])
# Insert at position 2
my_list.insert(1, 15)
# Extend
my_list.extend([50,60,70])

# Remove the last element
my_list.pop()

# SORT LIST IN ASSENDING ORDER
my_list.sort()

# Find and print the index of the value 30 in my_list
print(my_list.index(30))