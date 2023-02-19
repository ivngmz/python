# First example

def mean(my_list_in):
    the_mean = sum(my_list_in) / len(my_list_in)
    return the_mean


my_list = [1, 3, 4]

print(mean(my_list))

# Types of functions:

print('There are two types of functions:')
print('1. First is the function I have yet created')
print(type(mean))
print('2. Other is functions that exists on builtins')
print(type(sum))
print('Remember how to get info about builtins:')
print(dir(__builtins__))


# Another example:

def convert(amount):
    output = amount * 1.75
    return output


print(convert(150))


# A function without return sentence:


def query():
    print('query')


print('Here we have the object returned when we call a function without return:')
print(query())
print('"None" is an specific object that means nothing')
