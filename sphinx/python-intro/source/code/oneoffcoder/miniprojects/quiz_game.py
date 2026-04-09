import json
import random


QUESTIONS = json.loads(
    """
    [
      {"question": "2 + 2 = ?", "answer": "4"},
      {"question": "Capital of France?", "answer": "paris"},
      {"question": "Python file extension?", "answer": ".py"}
    ]
    """
)

random.shuffle(QUESTIONS)
score = 0

for item in QUESTIONS:
    print(item['question'])
    guess = input('> ').strip().lower()
    if guess == item['answer']:
        score += 1
        print('correct')
    else:
        print(f"wrong, expected {item['answer']}")

print(f'score: {score}/{len(QUESTIONS)}')
