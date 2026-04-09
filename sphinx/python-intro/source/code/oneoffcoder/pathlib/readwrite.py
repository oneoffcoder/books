from pathlib import Path


path = Path('hello.txt')
path.write_text('Hello, world!\n', encoding='utf-8')

contents = path.read_text(encoding='utf-8')
print(contents)
