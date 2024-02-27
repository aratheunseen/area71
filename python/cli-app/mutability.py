filenames = ['file1.t.x.t', 'file2.txt', 'file3.txt']

for filename in filenames:
    filename = filename.replace(".", "")
    filename = filename.replace("txt", ".txt")
    print(filename)

print(filenames)