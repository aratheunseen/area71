prompt = "Type add, show, edit or complete:"
todos = open("todos.txt").read().splitlines()

while True:
    user_action = input(prompt)
    
    match user_action:
        case "add":
            todo = input("Enter a task: ")
            if todo == "done":
                break
            file = open("todos.txt", "a")
            file.write(todo + "\n")

        case "show":
            for item_id,item in enumerate(todos):
                # print(item_id+1,"-",item)
                print(f"{item_id+1}- {item}")

        case "edit":
            number = int(input("Enter the number of the task to edit: "))
            existing_task = todos[number-1]
            print("Editing task", existing_task)
            new_task = input("Enter the new task: ")
            todos[number-1] = new_task

        case 'complete':
            number = int(input("Enter the number of the task to complete: "))
            completed_task = todos.pop(number-1)
            print("Completed task", completed_task, ", removed from list")
        
        case _:
            print("Invalid user action")