# to use pandas you firstly need to install
#   pip3.9.exe install pandas
# In the next lecture, you will learn how to load Excel files in Python with pandas.
# For this, you need pandas (which you have already installed) and also two other dependencies that pandas needs for opening Excel files
# You can install them with pip:
#   pip3.9 install openpyxl (needed to load Excel .xlsx files)
#   pip3.9 install xlrd (needed to load Excel old .xls files)

# 
import os
print(os.listdir())
path_file=os.path.abspath(os.path.join(os.path.dirname(__file__)))

import pandas
sf1 = pandas.read_csv(path_file + "/supermarkets.csv")
print(sf1)

import pandas
sf1 = pandas.read_json(path_file + "/supermarkets.json")
print(sf1)

import pandas
df3 = pandas.read_excel(path_file + "/supermarkets.xlsx",sheet_name=0)
print(df3)