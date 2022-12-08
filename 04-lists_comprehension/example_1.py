# temps = [221,234,340,230]
# new_tems = []

# print("This is the contents before for list temps:")
# print(temps)
# print("This is the contents after for list new_tems:")
# print(new_tems)

# for temp in temps:
#     new_tems.append(temp/10)
# print("This is the contents before for list temps:")
# print(temps)
# print("This is the contents after for list new_tems:")
# print(new_tems)



# print("Another example!!")

# temps = [221,234,340,230]
# new_tems = []

# print("This is the contents before for list temps:")
# print(temps)
# print("This is the contents before for list new_tems:")
# print(new_tems)

# for temp in list(range(len(temps)-1,-1,-1)):
#     item = temps.pop(temp)
#     new_tems.append(item/10)
#     print("Iteration number: " + str(temp+1))
#     print("This is the contents for list temps:")
#     print(temps)
#     print("This is the contents for list new_tems:")
#     print(new_tems)
    
print("Another example!!!!")
print("list comprehension")

temps = [221,234,340,230]
new_temps = [temp/10 for temp in temps]
print(new_temps)

print("Another example!!!!")
print("list comprehension")

temps = [221,234,340,230]
new_temps = [temp/10 for temp in temps if temp != 230]
print(new_temps)
print(":)")

print("Another example!!!!")
print("list comprehension")

temps = [221,234,340,230]
new_temps = [temp/10 if temp != 221 else 0 for temp in temps]
print(new_temps)