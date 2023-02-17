# The simpliest example to test:
print('#####################################################################################################################################')
print('hello')
print('#####################################################################################################################################')
print('In the next example we are going to sum two numbers')
print('7 and 9 equals to: calculating ...')
print(7 + 9)
print('#####################################################################################################################################')
print('Now we are going to use some variables to make a sum of numbers...')
items = 10
price = 2
total_price = items * price
print('#####################################################################################################################################')
# Below we print out three variables
print('total_price items price') 
print(total_price, items, price) 
print('#####################################################################################################################################')
#  Now we are going to store information
print('A list, in the form of: example_list = [10.4, 1, "good"]')
example_list = [10.4, 1, "good"]
print(example_list)
print('What about a more complex list: complex_list = [3.02, 2, \'shop\', [42, 31, 2]]')
complex_list = [3.02, 2, 'shop', [42, 31, 2]]
print(complex_list)
print('#####################################################################################################################################')
print('How to use range function:')
print(list(range(0, 110)))
print('#####################################################################################################################################')
print('How to use dictionary: temps = {\'morning\': 5.1, \'noon\': 6.1, \'evening\': 10.2}')
temps = {'morning': 5.1, 'noon': 6.1, 'evening': 10.2}
print('this is the output for stored var: ' + str(temps))
print('And now an example: How to get an item:')
print(temps.items())
print(temps.keys())
print(temps.values())
print('#####################################################################################################################################')
print('This is a tuple: (2,3,4) and it is unmutable')
tuple_example = (2, 3, 4)
print(tuple_example)
# Well done, some more!!!
print('How to get help with interactive shell:')
print('Easy, use dir() command, you could try it by using interactive interpreter...')
print('>>> dir()')
print('the attributes used internally are thos who starts with underscore, the rest are methods')
print('One more thing, what happens if you use: dir(list)')
print('This is more interesting: help(list) and help(list.copy)')
print('This is the best way to get information quickly!')
print('other important a note, what about functions:  dir(__builtins__)')
print('Example: count help(list.count), if we use it with: [1, 10.0, 9.9, 10.0]')
grades = [1, 10.0, 9.9, 10.0]
print(grades.count(10.0))

