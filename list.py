## Creating lists ##

# Enter values directly into square brackets
list_of_numbers = [1, 2, 3]
print('list_of_numbers:', list_of_numbers)

# Using list constructor
list_of_names = list(('ram', 'suresh', 'ramesh'))
print('list_of_names:', list_of_names)

## Adding an element to existing list ##

# At last
new_number_1 = 4
list_of_numbers.append(new_number_1)
print('list_of_numbers after appending a number:', list_of_numbers)

# At a specific index(Always index starts from 0)
new_name_1 = 'rajesh'
list_of_names.insert(1, new_name_1)
print('list_of_names after inserting a name:', list_of_names)

## Extend an existing list with another list ##

# Creating a new list then extending old list
new_list_of_numbers = [10, 11, 12]
list_of_numbers.extend(new_list_of_numbers)
print('list_of_numbers after extending the current list:', list_of_numbers)

# Note: If you extending with a unknown type always use "or" operator,
# Which passes an empty array instead of None and avoids raise of exception.
new_list_of_names = None
list_of_numbers.extend(new_list_of_names or [])
print('list_of_names after extending the current list:', list_of_names)

## Accessing a list elements

# print third element of a list, here 2 is the index as index starts with 0.
print('Third element of list_of_numbers:', list_of_numbers[2])

# Getting the index of an element present in the list
print('list_of_numbers.index(3):', list_of_numbers.index(3))

# Getting the index of an element not present in the list
print('list_of_numbers.index(3, 1, 5):', list_of_numbers.index(3, 1, 5))

## Remove an element from an list


