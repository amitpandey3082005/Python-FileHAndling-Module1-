with open("notes.txt", "r", encoding="utf-8") as file:
    data = file.read()
    print(data)

# No file.close() is required here.
# Python closes it automatically!
