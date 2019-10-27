import tempfile

# write to a temporary file
with tempfile.NamedTemporaryFile(delete=False) as f:
    print(f'writing to {f.name}')
    f.write(b'oneoffcoder.com')

# read from temporary file
with open(f.name, 'r') as rf:
    print(rf.read())

# create a temporary directory
with tempfile.TemporaryDirectory() as d:
    print(f'created temporary directory {d}')
