def get_todos(filepath):
    """ Read a text file and return the list of todos from the file. """
    with open(filepath, 'r') as get_file:
        todos_loc = get_file.readlines()
    return todos_loc

def set_todos(filepath,todos):
    """ Write the todo items list int the text file. """
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

    elif user_action.startswith("help "):
        command = user_action[5:]
        if command == 'add':
            print("\n\tType 'add <your_note>' to add a new note.\n")
        elif command == 'show':
            print("\n\tType 'show' to view all todo items.\n")
        elif command == 'edit':
            print("\n\tType 'edit <number_of_old_todo> <new_note>'" 
                   " to view all todo items.\n")

    else:
        print("Invalid input.")