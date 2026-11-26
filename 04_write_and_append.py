# WRITE MODE — 'w'
with open("report.txt", "w", encoding="utf-8") as f:
    f.write("Python File Handling\n")
    f.write("This is a new report.\n")

# APPEND MODE — 'a'
with open("report.txt", "a", encoding="utf-8") as f:
    f.write("This line is appended.\n")
