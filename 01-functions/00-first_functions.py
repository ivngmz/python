# First example

def mean(my_list):
    the_mean = sum(my_list) / len(my_list)
    return the_mean
    
#my_list=('eat','to','much')
my_list=[1,3,4]

print(mean(my_list))

# Types of functions:

print('There are two types of functions:')
print('First is the function I have created')
print(type(mean))
print('This a function that exists')
print(type(sum))
print('Remember:')
print(dir(__builtins__))

# Another example:

def convert(amount):
    output = amount * 1.75
    return output
 
print(convert(150))

# A function without return sentence:


def query():
    query_stc = print('query')

print('Here we have the object returned when we call a function without return:')
print(query())
print('"None" is an especific object that means nothing')