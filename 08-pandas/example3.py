import pandas
import os
path_file=os.path.abspath(os.path.join(os.path.dirname(__file__)))

# If the csv does not have no header:
df6 = pandas.read_csv(path_file + "/supermarkets-commas2.txt", header = None)
# print(df6)

# you also can add headers:

df6.columns=["ID","Address","City","State","Country","Name","Employees"]

print(df6)

print("we also can select index column")
df6.set_index("Address")
print(df6)

df7=df6.set_index("ID")
# df6.set_index("Address", inplace = True, drop = False)
print(df7)