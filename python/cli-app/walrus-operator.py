prompt = "Enter your password:"

while password := input(prompt): # colon equal operator (walrus operator) is used to assign a value to a variable as part of an expression
    if password == "1234":
        print("Access granted!")
        print("Homepage Loading...")
        print("Hi, welcome to the system!")
        break

    if password != "1234":
        print("Invalid password")
        continue