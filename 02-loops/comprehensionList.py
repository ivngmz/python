temps = [221, 234, 340, 230]

new_temps = []

# -------------------------------------------------------- 
# for temp in temps:
#     new_temps.append(temp/10)

# print(new_temps)

# -------------------------------------------------------- 
# new_temps = [temp / 10 for temp in temps]

# print(new_temps)
# -------------------------------------------------------- 

# new_temps = [temp / 10 for temp in temps if temp != 221]

# print(new_temps)

# -------------------------------------------------------- 

new_temps = [temp / 10 if temp != 221 else 0 for temp in temps]

print(new_temps)