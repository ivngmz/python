import os

path_file=os.path.abspath(os.path.join(os.path.dirname(__file__)))
file_name="fruits.txt"
myfile = open(path_file + "/" + file_name)

content = myfile.read()
myfile.close()

print(content)

################################
#
# import os

# path_file=os.path.abspath(os.path.join(os.path.dirname(__file__)))
# file_name="fruits.txt"

# with open(path_file + "/" + file_name) as myfile:
#     content = myfile.read()
# print(content)