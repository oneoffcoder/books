command = 'start'

match command:
    case 'start':
        print('starting')
    case 'stop':
        print('stopping')
    case 'pause':
        print('pausing')
    case _:
        print('unknown command')
