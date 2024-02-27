prompt = "Enter your todo:"
todos = []

while True:
    todo = input(prompt)
    todo.capitalize()

    if todo == "exit":
        break

    if todo == "show":
        print(todos)
        continue

    if todo == "remove":
        todos.pop()
        continue

    if todo == "clear":
        todos.clear()
        continue

    if todo == "remove x":
        name = input("Enter the name of the todo to remove: ")
        todos.remove(name)
        continue
        

    todos.append(todo)
    print(todos)