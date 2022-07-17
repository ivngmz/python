# student_grades = {"Maria": 9.1, "Juan": 8.2}

# for grades in student_grades.values():
#     print(grades)


# phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
     
# for key, value in phone_numbers.items():
#     print("{} has as phone number {}".format(key, value))

languages = {"Español": "es","Frances": "fr","aleman": "de","Checo": "cs"}
        
for key, value in languages.items():
    url = "/todos/""/"+str(value)
    print(url)
    print('Response Get Todo: '+str(key)+': ')