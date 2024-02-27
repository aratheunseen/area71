prompt = "Add a new member: "

while True:
    name = input(prompt)
    if name == "q":
        break

    file = open("members.txt","r")
    members = file.readlines()
    file.close()

    members.append(name+"\n")
    file = open("members.txt","w")
    file.writelines(members)
    file.close()
