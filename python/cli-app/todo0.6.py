while True:
    user_action = input("YourNote > ")
    user_action = user_action.strip()
    
    if user_action.startswith("add "):
        todo = user_action[4:]
    
        with open('todos.txt', 'r') as file:
            todos = file.readlines()
        
        todos.append(todo+"\n")

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif user_action.startswith("show"):

        with open("todos.txt","r") as file:
            todos = file.readlines()

        for todo_id, todo in enumerate(todos):
            print(todo_id+1,"-",todo.strip())

    elif user_action.startswith("edit "):
        try:
            number = int(user_action[5:7])
            new_todo = user_action[7:]

            with open("todos.txt","r") as file:
                todos = file.readlines()
            
            todos[number-1] = new_todo + '\n'

            with open("todos.txt","w") as file:
                file.writelines(todos)

        except ValueError:
            print("Invalid command.")

    elif user_action.startswith("complete"):
        
        try:
            number = int(user_action[9:])
            
            with open("todos.txt","r") as file:
                todos = file.readlines()

            completed_todo = todos.pop(number-1)

            with open("todos.txt","w") as file:
                file.writelines(todos)
            
            print(f"{completed_todo.strip()} is removed from the todo list.")
        
        except ValueError:
            print("Error in value.")

        except IndexError:
            print("Error in Index.")

        except SyntaxError:
            print("Lol in Syntex")

    elif user_action.startswith("exit"):
        break 

    else:
        print("Invalid input.")