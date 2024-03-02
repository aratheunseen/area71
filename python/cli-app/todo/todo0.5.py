while True:
    user_action = input("YourNote > ")
    user_action = user_action.strip()
    
    if "add" in user_action or "new" in user_action:
        todo = user_action[4:]
    
        with open('todos.txt', 'r') as file:
            todos = file.readlines()
        
        todos.append(todo+"\n")

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif "show" in user_action or "display" in user_action:

        with open("todos.txt","r") as file:
            todos = file.readlines()

        for todo_id, todo in enumerate(todos):
            print(todo_id+1,"-",todo.strip())

    elif "edit" in user_action:
        number = int(user_action[5:7])
        new_todo = user_action[7:]

        with open("todos.txt","r") as file:
            todos = file.readlines()
        
        todos[number-1] = new_todo + '\n'

        with open("todos.txt","w") as file:
            file.writelines(todos)

    elif 'complete' in user_action:
        number = int(user_action[-1:])
        
        with open("todos.txt","r") as file:
            todos = file.readlines()

        completed_todo = todos.pop(number-1)

        with open("todos.txt","w") as file:
            file.writelines(todos)
        
        print(f"{completed_todo.strip()} is removed from the todo list.")

    elif 'exit' in user_action:
        break 

    else:
        print("Invalid input.")