temperatures = [10, 12, 14]
file = open("file.txt", 'w')
temperatures = [str(temp) + "\n" for temp in temperatures]
file.writelines(temperatures)