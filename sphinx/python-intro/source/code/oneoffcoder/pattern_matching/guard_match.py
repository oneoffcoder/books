point = (3, 4)

match point:
    case (x, y) if x == y:
        print('same coordinates')
    case (x, y) if x > y:
        print('x is larger')
    case (x, y):
        print('y is larger or equal')
