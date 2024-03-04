# Create a program that prompts the user to input their name repeatedly. Then, the program repeatedly prints out the name with the first letter capitalized.

prompt = "Enter your name: "

while True:
    name = input(prompt)
    print(name.capitalize())