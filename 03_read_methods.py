# Assume sample.txt contains:
# Python is easy to learn.
# File handling stores data.

with open("sample.txt", "r", encoding="utf-8") as f:
    all_text = f.read()
    print(all_text)
