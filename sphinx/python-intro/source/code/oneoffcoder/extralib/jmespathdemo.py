import jmespath

planets = {
    'planets': [
        {'name': 'mercury', 'is_solid': True},
        {'name': 'venus', 'is_solid': True},
        {'name': 'earth', 'is_solid': True},
        {'name': 'mars', 'is_solid': True},
        {'name': 'jupiter', 'is_solid': False},
        {'name': 'saturn', 'is_solid': False},
        {'name': 'uranus', 'is_solid': False},
        {'name': 'neptune', 'is_solid': False},
    ]
}

print(jmespath.search('planets[*].name', planets))
print(jmespath.search('planets[*].is_solid', planets))