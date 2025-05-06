from pathlib import Path

path = Path("README.md")

print("path.exists():", path.exists())
print("path.is_dir():", path.is_dir())
print("path.is_file():", path.is_file())
print("path.name:", path.name)
print("path.stem:", path.stem)
print("path.suffix:", path.suffix)
print("path.parent:", path.parent)
print("path.absolute():", path.absolute())
print("path.resolve():", path.resolve())
print("path.stat():", path.stat())

path = path.with_suffix(".txt")
print(path)
