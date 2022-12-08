user_prompt = "Enter a todo: "
todos = ["List of inputs:"]

cicles: int = 4
while cicles > 1:
    todo = input(user_prompt)
    todos.append(todo)
    cicles -= 1

print(todos)

print(type(todos))
