# Get a input via terminal window
number_1 =  input('Enter a number: ')

# By default all input are considered as string,
# so must cast it to int.
## Note: I assume the number_1 can be casted into integer type.
number_1 = int(number_1)

# Print the absolute of the number
print('Absolute of number is:', abs(int(number_1)))