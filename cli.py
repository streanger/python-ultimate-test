import sys
from pathlib import Path

class Colors:
    RESET = '\033[0m'
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'

questions = Path('questions.txt').read_text().splitlines()
questions = [line.strip() for line in questions if line.strip()]
questions_number = len(questions)

# ask questsions
points = 0
for index, question in enumerate(questions, start=1):
    answer = input(f'{index}. {question} (y/n) ')
    if answer.lower().startswith('y'):
        points += 1

# score
levels = {
    range(0, 10): "Noob",
    range(10, 20): "Beginner",
    range(20, 30): "Advanced",
    range(30, 40): "Python Enthusiast",
    range(40, 50): "Snake Charmer",
    range(50, 51): "Pythonist"
}
for r, name in levels.items():
    if points in r:
        result = name
        break
else:
    print(f'out of range: {points}')
    sys.exit(-1)

print(f'\n{20*"-"}')
print(f'your score is: {Colors.CYAN}{points}/{questions_number}{Colors.RESET}')
print(f'you are: {Colors.CYAN}{result}{Colors.RESET}')
