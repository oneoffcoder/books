type ScoresByUser = dict[str, list[int]]


def top_score(data: ScoresByUser, user: str) -> int | None:
    scores = data.get(user)
    if not scores:
        return None
    return max(scores)


print(top_score({'jane': [88, 93, 91]}, 'jane'))
print(top_score({}, 'john'))
