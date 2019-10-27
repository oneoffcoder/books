from datetime import timedelta

# compute difference between durations using timedelta
a = timedelta(weeks=2, days=2, hours=1, seconds=30)
b = timedelta(weeks=1, days=2, hours=1, seconds=30)
diff = a - b
print(diff)

