print("In this case we are going to work with csv")
import os
path_file=os.path.abspath(os.path.join(os.path.dirname(__file__)))

import pandas
df4=pandas.read_csv(path_file + "/supermarkets-commas.txt")
print(df4)

import pandas
df5=pandas.read_csv(path_file + "/supermarkets-semi-colons.txt",sep=";")
print(df5)
