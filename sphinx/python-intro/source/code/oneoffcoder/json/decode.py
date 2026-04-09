import json

raw = '{"name": "Ava", "scores": [95, 88, 91], "active": true}'
payload = json.loads(raw)

print(payload['name'])
print(payload['scores'])
print(payload['active'])
