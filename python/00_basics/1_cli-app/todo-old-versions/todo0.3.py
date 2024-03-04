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
                file = open("todos.txt","a+")
                file.writelines(todo)
                file.close()
                print("Todo added")

        case "show":
            file = open("todos.txt","r")
            todos = file.readlines()
            for id, todo in enumerate(todos):
                print(id+1, todo.strip())
            file.close()

        case "edit":
            number = int(input("Enter the number of the task to edit: "))
            existing_task = todos[number-1]
            print("Editing task", existing_task)
            new_task = input("Enter the new task: ")
            todos[number-1] = new_task
            file = open("todos.txt","w")
            file.writelines(todos)
            file.close()

        case 'complete':
            number = int(input("Enter the number of the task to complete: "))
            completed_task = todos.pop(number-1)
            print("Completed task", completed_task, ", removed from list")
        
        case 'exit':
            break

        case _:
            print("Invalid user action.")