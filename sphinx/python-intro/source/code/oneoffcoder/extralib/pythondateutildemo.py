from dateutil.parser import parse

logline = 'INFO 2021-12-31T23:59:11 Almost new year!'
timestamp = parse(logline, fuzzy=True)
print(timestamp)