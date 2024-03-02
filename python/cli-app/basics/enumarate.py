words = ["apple","ball","cat","dog"]

for index, word in enumerate(words):
    print(f"{index+1}: {word}")

print("\n\nEnumerate Analysis:")
print(enumerate(words))
print(list(enumerate(words)), "\n\n") # list of tuples
