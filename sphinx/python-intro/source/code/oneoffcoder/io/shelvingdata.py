import shelve

data = {f'x{x}': {f'y{y}': y for y in range(100)} for x in range(100)}

# shelving data
with shelve.open('data.s') as s:
    s['data'] = data

# unshelving data
with shelve.open('data.s') as s:
    data = s['data']
    print(data)
