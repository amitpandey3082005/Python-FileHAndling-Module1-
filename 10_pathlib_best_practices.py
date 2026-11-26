from pathlib import Path

file_path = Path("data") / "notes.txt"
file_path.parent.mkdir(parents=True, exist_ok=True)
file_path.write_text("Hello!", encoding="utf-8")
print(file_path.read_text(encoding="utf-8"))
