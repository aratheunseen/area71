prompt = "Type add, show, edit or complete:"

while True:
    user_action = input(prompt)
    
    match user_action:

        case "add":

            todo = ""
            while todo != "q\n":
                todo = input("Enter a todo or 'q' to quit: ") + "\n"
                if todo == "q\n":
                    break
                
                with open('todos.txt', 'r') as file:
                    todos = file.readlines()
                
                todos.append(todo)

                with open('todos.txt', 'w') as file:
                    file.writelines(todos)

        case "show":

            with open("todos.txt","r") as file:
                todos = file.readlines()

            for todo_id, todo in enumerate(todos):
                print(todo_id+1, todo.strip())

        case "edit":

            number = int(input("Enter the number of the todo to edit: "))
            todos[number-1] = input("Enter the new todo: ") + '\n'

            with open("todos.txt","w") as file:
                file.writelines(todos)

        case 'complete':

            number = int(input("Enter the number of the task to complete: "))
            
            with open("todos.txt","r") as file:
                todos = file.readlines()

            completed_todo = todos.pop(number-1)

            with open("todos.txt","w") as file:
                file.writelines(todos)
            
            print(f"{completed_todo.strip()} is removed from the todo list.")

        case 'exit':
            break 

        case _:
            print("Invalid input.")