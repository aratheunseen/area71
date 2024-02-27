while True:
    prompt = input("Enter your todo: ")

    todo = open("todo.txt", "a")
    todo.write(prompt + "\n")
    todo.close()

    if prompt == "exit":
        break

print("Todo added successfully!")
print("Your todo list is: ")
todo = open("todo.txt", "r")
print(todo.read())
todo.close()