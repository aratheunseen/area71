prompt = "Type add or show: "
todos = []

while True:
    command = input(prompt)
    
    match command:
        case "add":
            while True:
                task = input("Enter a task: ")
                todos.append(task)

                if input("Add another? (yes/no) ") == "no":
                    break

        case "show":
            print(todos)
        case _:
            print("Invalid command")