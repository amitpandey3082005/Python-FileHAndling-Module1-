# Copy an image or PDF without changing bytes
source = "input.pdf"
destination = "input_copy.pdf"

with open(source, "rb") as src:
    data = src.read()

with open(destination, "wb") as dest:
    dest.write(data)

print("File copied successfully!")
