# We are going to use Nominatim() in the next video. Nominatim() currently has a bug. To fix this problem, whenever you see these lines in the next video:
# pip install geopy
# from geopy.geocoders import Nominatim
# nom = Nominatim()

# change them to these

from geopy.geocoders import ArcGIS
nom = ArcGIS()
import os
path_file=os.path.abspath(os.path.join(os.path.dirname(__file__)))

# The rest of the code remains the same.
# n = nom.geocode("3995 23rd St, San Francisco, CA 94114")
# print(n)

import pandas
df = pandas.read_csv(path_file + "/supermarkets.csv")
df["Address"]=df["Address"]+", "+df["City"]+", "+df["State"]+", "+df["Country"]
print(df)

df["Coordinates"] = df["Address"].apply(nom.geocode)
print(df.Coordinates)
# # print(df.Coordinates[0].latitud)

# df["Latitud"]=df["Coordinates"].apply(lambda x: x.latitud if x != None else None)