tasks = []

def add_task(task):
    tasks.append(task)

def show_tasks():
    for index, task in enumerate(tasks, 1):
        print(f"{index}. {task}")

add_task("Learn Python")
add_task("Build GitHub project")
add_task("Practice programming")

show_tasks()
