
# TODO решите задачу
import json

def task() -> float:
    filename = "input.json"  # фиксированное имя файла
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)

    total = 0.0
    for item in data:
        total += item.get("score", 0) * item.get("weight", 0)

    return round(total, 3)

print(task())