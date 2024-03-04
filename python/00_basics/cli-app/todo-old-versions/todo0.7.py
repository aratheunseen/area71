def get_todos(filepath):
    with open(filepath, 'r') as get_file:
        todos_loc = get_file.readlines()
    return todos_loc

def set_todos(filepath,todos):
    with open(filepath, 'w') as set_file:
        set_file.writelines(todos)

while True:
    user_action = input("YourNote > ")
    user_action = user_action.strip()
    
    if user_action.startswith("add "):
        todo = user_action[4:]
        todos = get_todos('todos.txt')
        todos.append(todo+"\n")
        set_todos('todos.txt',todos)

    elif user_action.startswith("show"):
        todos = get_todos('todos.txt')
        for todo_id, todo in enumerate(todos):
            print(todo_id+1,"-",todo.strip())

    elif user_action.startswith("edit "):
        try:
            number = int(user_action[5:7])
            new_todo = user_action[7:]
            todos = get_todos('todos.txt')
            todos[number-1] = new_todo + '\n'
            set_todos('todos.txt',todos)

        except ValueError:
            print("Invalid command.")

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            todos = get_todos('todos.txt')
            completed_todo = todos.pop(number-1)
            set_todos('todos.txt',todos)
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