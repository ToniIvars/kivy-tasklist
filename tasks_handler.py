import json
from typing import List, Tuple

def add_task(task_id: int, task_name: str) -> None:
    task_id = str(task_id)

    with open('tasks.json', 'r', encoding='utf-8') as f:
        tasks = json.load(f)

    tasks[task_id] = task_name

    with open('tasks.json', 'w', encoding='utf-8') as f:
        json.dump(tasks, f, indent=4)

def remove_task(task_id: int) -> None:
    task_id = str(task_id)

    with open('tasks.json', 'r', encoding='utf-8') as f:
        tasks = json.load(f)

    tasks.pop(task_id)

    with open('tasks.json', 'w', encoding='utf-8') as f:
        json.dump(tasks, f, indent=4)

def get_tasks() -> List[Tuple]:
    with open('tasks.json', 'r', encoding='utf-8') as f:
        tasks = json.load(f)

    return [(int(index), text) for index, text in tasks.items()]