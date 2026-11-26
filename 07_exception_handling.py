try:
    with open("students.txt", "r", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("Error: students.txt was not found.")
except PermissionError:
    print("Error: permission denied.")
except OSError as error:
    print("File error:", error)
