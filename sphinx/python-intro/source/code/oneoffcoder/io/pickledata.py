import pickle

data = {f'x{x}': {f'y{y}': y for y in range(100)} for x in range(100)}

# pickle data
with open('data.p', 'wb') as f:
    pickle.dump(data, f)

# unpickle data
with open('data.p', 'rb') as f:
    data = pickle.load(f)
    print(data)
