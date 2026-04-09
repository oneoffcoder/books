from pathlib import Path


path = Path('notes.txt')

print(path.exists())
print(path.is_file())
print(path.suffix)
