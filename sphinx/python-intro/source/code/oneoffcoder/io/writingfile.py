with open('data.csv', 'w') as f:
    for r in range(100):
        s = ','.join([str(c) for c in range(100)])
        f.write(s)
        f.write('\n')
