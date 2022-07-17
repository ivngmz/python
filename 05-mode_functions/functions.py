import time


print("We start this exercise by printing some help:")
time.sleep(2)
help_len=str(help(len))
help_isinstance=str(help(isinstance))

# non key-word arguments
def area(a, b):
    return a * b

print(area(4,5))


# argument parameter
def area(a, b):
    return a * b

print(area(b=4,a=5))


# default parameter, allways after non default parameters
def area(a, b=2):
    return a * b

print(area(4,5))

# using args
def mean(*args):
    return sum(args)/len(args)

print(mean(3,277,6))

def foo(*args):
    args = [x.upper() for x in args]
    return sorted(args)

print(foo("river","sea","lake"))

# using kwargs
def mean(**kwargs):
    return sum(kwargs.values())/len(kwargs)

print(mean(a=3,b=277,c=6))


def find_sum(**kwargs):
    return sum(kwargs.values())
    
print(find_sum(x=1, y=2, z=6))