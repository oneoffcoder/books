from datetime import datetime
from zoneinfo import ZoneInfo


ny_time = datetime(2025, 1, 15, 9, 0, tzinfo=ZoneInfo('America/New_York'))
london_time = ny_time.astimezone(ZoneInfo('Europe/London'))

print(ny_time)
print(london_time)
