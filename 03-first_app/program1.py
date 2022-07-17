# Program  that ask you for input and end with "\end". Then write the previos inputs

members = []
while True:
    memberssmsg = input("Say Something: ")
    if memberssmsg == "\end":
        break
    else:
        members.append(memberssmsg)

print(members)