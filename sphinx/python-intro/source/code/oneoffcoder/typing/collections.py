def average(numbers: list[float]) -> float:
    return sum(numbers) / len(numbers)


def word_counts(words: list[str]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts


print(average([2.0, 4.0, 6.0]))
print(word_counts(['red', 'blue', 'red']))
