import os
import random
from datetime import datetime, timedelta

# Exercise 5.1


def find_pdf_size(top):
    total_size = 0
    for root, dirs, files in os.walk(top):
        for file in files:
            if file.lower().endswith(".pdf"):
                path = os.path.join(root, file)
                try:
                    total_size += os.path.getsize(path)
                except OSError:
                    continue
    return total_size


print(f"Total PDF size: {find_pdf_size('.')} bytes")

# Exercise 5.2


def print_working_days(date1, date2):
    start = datetime.strptime(date1, "%Y-%m-%d")
    end = datetime.strptime(date2, "%Y-%m-%d")

    current = start
    while current < end:
        if current.weekday() < 5:
            print(current.strftime("%Y-%m-%d"))
        current += timedelta(days=1)


# Exercise 5.3


def random_walk(start):
    x = start
    while True:
        yield x
        x = x + random.choice([-1, 1])


def run_experiment(steps=100):
    walker = random_walk(0)
    pos = 0
    for _ in range(steps + 1):
        pos = next(walker)
    return pos


print("Final positions after 100 moves:")
for i in range(1, 16):
    final_pos = run_experiment(100)
    print(f"Experiment {i}: {final_pos}")
