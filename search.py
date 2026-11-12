def search_task(tasks, keyword):
    return [
        task for task in tasks
        if keyword.lower() in task.title.lower()
    ]