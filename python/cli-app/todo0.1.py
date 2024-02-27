prompt = "Type add, show or edit: "
todos = []

while True:
    command = input(prompt)
    
    match command:
        case "add":
            task = ""
            while task != "done":
                task = input("Enter a task: ")
                if task == "done":
                    break
                todos.append(task)

        case "show":
            for item_id,item in enumerate(todos):
                print(item_id+1,"-",item)

        case "edit":
            index = int(input("Enter the number of the task to edit: "))
            new_task = input("Enter the new task: ")
            todos[index-1] = new_task

        case _:
            print("Invalid command")