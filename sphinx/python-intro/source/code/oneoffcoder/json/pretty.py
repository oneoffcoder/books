import json

payload = {
    'course': 'Python',
    'students': ['Ava', 'Noah', 'Mia'],
    'count': 3,
}

print(json.dumps(payload, indent=2, sort_keys=True))
