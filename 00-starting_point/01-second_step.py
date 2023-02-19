print('#####################################################################################################################################')
print('Working with lists')
list_example = [2.23, 1.43, 1.04]
item_example = 1.11
print('list_example = ' + str(list_example) + ' appended with item_example = ' + str(item_example))
print('result to append') 
list_example.append(item_example)
print(list_example)
print('removing an item: 1.43')
list_example.remove(1.43)
print(list_example)
print('accessing to item 2 (index 2)')
print(list_example[2])
print('this is named list slice: 1:')
print(list_example[1:])
print('accessing in reverse order: -2')
print(list_example[-2])
print('#####################################################################################################################################')
print('accessing to dictionaries:')
temps = {'morning': 5.1, 'noon': 6.1, 'evening': 10.2}
print(temps['evening'])
print('#####################################################################################################################################')
print('From tuple to list:')
cool_tuple = (1, 2, 3)
cool_list = list(cool_tuple)
print(cool_list)

print('From list to tuple:')
cool_list = [1, 2, 3]
cool_tuple = tuple(cool_list)
print(cool_tuple)

print('From string to list:')
cool_string = "Hello"
cool_list = list(cool_string)
print(cool_list)

print('From list to string:')
cool_list = ['H', 'e', 'l', 'l', 'o']
cool_string = str.join("", cool_list)
print(cool_string)
