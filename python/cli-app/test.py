# dir(str) -> list of attributes and methods of str
# help(str.upper) -> help on the upper method of str
# help(str) -> help on the str class

# import builtins -> built-in functions and classes
# dir(builtins) -> list of built-in functions and classes

prompt = "Type add or show: "
todos = []

while True:
    command = input(prompt)
    
    match command:
        case "add":
            while True:
                task = input("Enter a task: ")
                todos.append(task)

                if exit == "yes":
                    break

        case "show":
            for item in todos:
                print("-",item)
        case _:
            print("Invalid command")