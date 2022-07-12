def mean(input_object):
    if (type(input_object) is dict):
        print('Wow is a dict')
        result_is = sum(input_object.values()) / len(input_object)
        return result_is
    elif(type(input_object) is list):
        print('Wow is a list')
        result_is = sum(input_object) / len(input_object)
        return result_is
    else:
        return 'this is not type dict'
    
    
mydict = {"Jeremy": 33.1, "Sim": 21.3, "John": 99.5}
mylist = [342,42342,111,34123,342,6,67]

print('imagine you have a dictionary used as input for the function')
print(mean(mydict))
print('good, and now')
print('imagine you have a list used as input for the function')
print(mean(mylist))


print('Other options:')
if(type("abc") == str or type([1, 2, 3]) == list or isinstance("abc", str) or isinstance([1, 2, 3], list)):
    print('Ok')
else:
    print('Not Ok')
    
print('what about promt input:')

# def flavour(input_str):
#     if(isinstance(input_str,str)):
#         if(input_str in ['sweet','bitter']):
#             return('is a flavour I like')
#         else:
#             return('if it is a flavour, I dislike it')
#     else:
#         return ('It is needed to enter string to processs input')
    
# print(flavour('bitter'))
# print(flavour('saled'))
# print(flavour(input('enter a flavour: ')))
    
print('and how to format a string')

user_input = input("Enter your account: ")
message_content = "Hello %s?" % user_input
message_content1 = f"Hello {user_input}"
print(message_content)
print(message_content1)
surname_input = input("Please, enter your surname: ")
message_content2 = "Hello %s %s" % (user_input,surname_input)
print(message_content2)
message_content3 = f"Hello {user_input} {surname_input}"
print(message_content3)
message_content4 = "Your name is {}. Your surname is {}".format(user_input, surname_input)
print(message_content4)
