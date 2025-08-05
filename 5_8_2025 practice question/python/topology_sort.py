def task_scheduler(task_list, dependency_list):
    task_graph = {}
    task_count = {}
    
    for task in task_list:
        task_graph[task] = []
        task_count[task] = 0

    for task, before in dependency_list:
        task_graph[before].append(task)
        task_count[task] += 1

    ready_tasks = []
    for task in task_list:
        if task_count[task] == 0:
            ready_tasks.append(task)

    result = []
    while ready_tasks:
        current = ready_tasks.pop(0)
        result.append(current)

        for next_task in task_graph[current]:
            task_count[next_task] -= 1
            if task_count[next_task] == 0:
                ready_tasks.append(next_task)

    if len(result) == len(task_list):
        return result
    else:
        return None


examples = [
    {
        "name": "Test 1",
        "tasks": ["A", "B", "C", "D"],
        "dependencies": [("B", "A"), ("C", "B"), ("D", "A")]
    },
    {
        "name": "Test 2",
        "tasks": ["X", "Y", "Z"],
        "dependencies": [("Y", "X"), ("Z", "Y"), ("X", "Z")] 
    },
    {
        "name": "Test 3",
        "tasks": ["P", "Q", "R"],
        "dependencies": []
    },
    {
        "name": "Test 4",
        "tasks": ["compile", "test", "deploy", "build", "package"],
        "dependencies": [
            ("test", "compile"),
            ("deploy", "package"),
            ("package", "build"),
            ("build", "compile")
        ]
    }
]

for example in examples:
    print(f"{example['name']} Output:", task_scheduler(example["tasks"], example["dependencies"]))
