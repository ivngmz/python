import os
import time # builtin library
import os # standart library
import pandas # third party library

current_path=os.path.join(os.path.dirname(__file__))

while True:
    if os.path.exists(str(current_path + "/files/temps_today.csv")):
        data=pandas.read_csv(current_path + "/files/temps_today.csv")
        print(data.mean()["st1"])
    else:
        print("File does not exists")
    time.sleep(3)