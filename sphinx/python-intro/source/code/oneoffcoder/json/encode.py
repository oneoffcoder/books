import json

payload = {
    'name': 'Ava',
    'scores': [95, 88, 91],
    'active': True,
}

raw = json.dumps(payload)
print(raw)
