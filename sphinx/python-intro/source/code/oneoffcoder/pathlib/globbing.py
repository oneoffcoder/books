from pathlib import Path


for path in Path('.').glob('*.py'):
    print(path.name)
