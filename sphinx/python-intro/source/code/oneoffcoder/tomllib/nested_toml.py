import tomllib

with open('config.toml', 'rb') as f:
    config = tomllib.load(f)

print(config['database']['host'])
print(config['database']['port'])
