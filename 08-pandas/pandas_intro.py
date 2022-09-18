import pandas 

print("Pandas allow you to use data estructures:")
df1=pandas.DataFrame([[2,3,4],[10,32,33]])
print(df1)

print("If you want to assign a column name on each column...")

df1=pandas.DataFrame([[2,3,4],[10,32,33]],columns=["size","row","years"])
print(df1)

print("In this case,we also want to have a index name:")

df1=pandas.DataFrame([[2,3,4],[10,32,33]],columns=["size","row","years"],index=["first","second"])
print(df1)


print("You also can use a dictionary")
df2=pandas.DataFrame([{"key1":"Jane","key2":"Banday"},{"key1":"Tracy","key2":"Chaman"}])
print(df2)

print("You can use several methods to wortk with dataframes:")
print(str(dir(pandas.DataFrame)))
print(df1.mean())
print(df1.mean().mean())
print(type(df1.mean()))
print(df1.size.max())