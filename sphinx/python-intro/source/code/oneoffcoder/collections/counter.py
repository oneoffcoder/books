from collections import Counter


words = ['red', 'blue', 'red', 'green', 'blue', 'red']
counts = Counter(words)

print(counts)
print(counts['red'])
print(counts.most_common(2))
