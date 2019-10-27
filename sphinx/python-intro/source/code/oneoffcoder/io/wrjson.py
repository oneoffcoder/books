import json

data = {f'x{x}': {f'y{y}': y for y in range(100)} for x in range(100)}

# write json
with open('data.json', 'w') as f:
    f.write(json.dumps(data))

# write pretty json
with open('data.json', 'w') as f:
    f.write(json.dumps(data, indent=2))

# read json
with open('data.json', 'r') as f:
    s = json.load(f)
    print(s)
