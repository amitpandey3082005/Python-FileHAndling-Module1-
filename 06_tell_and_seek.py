with open("sample.txt", "r", encoding="utf-8") as f:
    print(f.tell())   # current position (0)
    print(f.read(6))  # read first 6 characters
    print(f.tell())   # position after reading (6)
    f.seek(0)         # move back to beginning
    print(f.read())   # read full file from start
