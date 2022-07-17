print("Instead of use only functions and builtin-functions, you also can use modules")
print("Below you can se an example about time module")
import sys
import time
print(dir(time))
print(help(time.sleep))

int_num=3
while int_num > 0:
    with open("fruits2.txt") as myfile:
        content = myfile.read()
        print(content)
        time.sleep(2)
        int_num=int_num-1
        
        
print("There is standart modules in pythons as time, yo can find tehm using:")
print(str(sys.prefix))
print("Using this path and entering in /lib(pythonX.Y...")
print("You can see a number of python files that are known as standart modules.")


print("On the other hand you have thrid party modules. You can find much of them in web. An exapmle is pandas: https://pandas.pydata.org/docs/ ")
print("You can import pandas: \"pip3 import pandas\"")