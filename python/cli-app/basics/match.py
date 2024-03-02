prompt = "Type add or show: "
todos = []

while True:
    command = input(prompt)
    command = command.lower().strip()
    
    match command:
        case "add":
            while True:
                task = input("Enter a task: ")
                todos.append(task)

                if input("Want to exit? (y/n) ") == "n":
                    break

        case "show":
            for item in todos:
                print("-",item)
        case _:
            print("Invalid command")