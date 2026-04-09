from datetime import datetime


dt = datetime(2025, 12, 31, 23, 45)
print(dt.strftime('%Y-%m-%d %H:%M'))

parsed = datetime.strptime('2025-12-31 23:45', '%Y-%m-%d %H:%M')
print(parsed)
