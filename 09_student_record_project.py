# Save a student record, then read it back
name = input("Enter student name: ")
marks = input("Enter marks: ")

with open("student_record.txt", "w", encoding="utf-8") as f:
    f.write(f"Name: {name}\n")
    f.write(f"Marks: {marks}\n")

print("\n--- Saved Record ---")
with open("student_record.txt", "r", encoding="utf-8") as f:
    print(f.read())
