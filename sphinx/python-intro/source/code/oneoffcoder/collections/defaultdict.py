from collections import defaultdict


grouped = defaultdict(list)

pairs = [('fruit', 'apple'), ('fruit', 'pear'), ('drink', 'water')]
for category, item in pairs:
    grouped[category].append(item)

print(grouped)
