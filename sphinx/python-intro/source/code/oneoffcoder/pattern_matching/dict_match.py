event = {'type': 'click', 'x': 10, 'y': 20}

match event:
    case {'type': 'click', 'x': x, 'y': y}:
        print(f'click at ({x}, {y})')
    case {'type': 'keypress', 'key': key}:
        print(f'key pressed: {key}')
    case _:
        print('unknown event')
