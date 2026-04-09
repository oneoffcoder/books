import tomllib

with open('config.toml', 'rb') as f:
    config = tomllib.load(f)

print(config['app']['name'])
print(config['app']['debug'])
