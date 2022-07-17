import os

path_file=os.path.abspath(os.path.join(os.path.dirname(__file__)))

with open(str(path_file) + "/fruits2.txt", "w") as myfile:
    myfile.write("Tomato\nCucumber\n")


with open(str(path_file) + "/fruits2.txt") as myfile:
    content = myfile.read()
print(content)

with open(str(path_file) + "/fruits2.txt", "a+") as myfile:
    myfile.write("Banana\nApple\nOrange\n")
    #seek method put cursor at Zero position
    myfile.seek(0)
    content = myfile.read()

print(content)