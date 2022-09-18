import pandas
import os
path_file=os.path.abspath(os.path.join(os.path.dirname(__file__)))

df7 = pandas.read_json(path_file + "/supermarkets.json")
print(df7)

df7.set_index("Address")
print(df7)
# print(df7.loc["735 Dolores St":"3995 23rd St","Address":"Employees"])
# print(df7.loc["735 Dolores St","Employees"])
print(df7.loc[:,"Address"])
print(df7.iloc[1:3,1:3])
# print(df7.iloc[:,1:3])
# print(df7.drop("City",1))
# df7.drop(df7.index[0:3],0)
# print(df7.index)
print(df7.columns)
print(len(df7.index))
df7["Continent"]=df7.shape[0]*["North America"]
print(df7)

df7["Continent"]=df7["Country"]+"," + "North America"
print(df7)

# Transposicion
df7_t=df7.T

print(df7_t)

# df7_t["My Address"]=["My City","My Country",10,7,"My Shop","My State","My Continent"]
# # print(df7_t)
# df7=df7_t