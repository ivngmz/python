heights = [1.86,1.67,1.89]

print(heights)


for x in heights:
    print(round(x))

heigth_sum=0.0
for x in heights:
    heigth_sum = heigth_sum + x
    print(round(heigth_sum))
    
def celsius_to_kelvin(cels):
    return cels + 273.15
 
for temperature in [9.1, 8.8, -270.15]:
    print(celsius_to_kelvin(temperature))
    
analisis_items = {'Joseph': 80, 'Rose': 45, 'Carl': 30}
for results in analisis_items.items():
    print(results)
for results in analisis_items.values():
    print(results)
for results in analisis_items.keys():
    print(results)
    
phone_numbers = {"John": "+37682929928", "Marry": "+423998200919"}
 
for pair in phone_numbers.items():
    print(f"{pair[0]} has as phone number {pair[1]}")

for key, value in phone_numbers.items():
    print(f"{key} has as phone number {value}")
    
    
