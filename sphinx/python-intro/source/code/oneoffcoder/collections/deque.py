from collections import deque


tasks = deque(['wash dishes', 'write report'])
tasks.append('call mom')
tasks.appendleft('drink coffee')

print(tasks.popleft())
print(tasks.pop())
print(tasks)
