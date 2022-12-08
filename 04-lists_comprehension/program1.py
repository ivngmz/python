from builtins import enumerate

todos = []


while True:
    user_action = input("Type action (add, show, complete, edit or exit): ")
    user_action = user_action.strip()
    if user_action == 'add':
        todo = input("Enter a todo: ")
        todos.append(todo)
        continue
    elif user_action == 'show':
        for index, item in enumerate(todos):
            row = f"{index + 1}-{item}"
            print(row)
        continue
    elif user_action == 'edit':
        number = int(input("Number of todo to edit: "))
        number = number - 1
        new_todo = input("Enter a todo to substitute previous: ")
        todos[number] = new_todo
        continue
    elif user_action == 'complete':
        rm_todo = int(input("Number of todo to remove: "))
        str_todo = todos[rm_todo - 1]
        todos.remove(str_todo)
        continue
    else:
        print("Printing list:" + str(todos))
        break
