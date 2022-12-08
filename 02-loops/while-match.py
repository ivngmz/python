comments_list =[]

while True:
    user_comment = input("Would you like to type a comment or no? (yes/no): ")

    if user_comment:
        if user_comment == 'yes':
            user_comment = input("Write the comment, please: ")
            comments_list.append(user_comment)
            continue
        elif user_comment == 'no':
            print("OK, maybe later")
            continue
        else:
            desire = input("Would you like to exit! (yes/no)?")
            if desire == 'yes':
                print("Bye")
                break
            else:
                continue
print("Printing list of your comments: " + str(comments_list))



