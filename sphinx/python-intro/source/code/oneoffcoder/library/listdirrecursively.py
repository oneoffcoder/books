import pathlib

py_files = pathlib.Path('../').glob('**/*.py')

for f in py_files:
    print(f)
