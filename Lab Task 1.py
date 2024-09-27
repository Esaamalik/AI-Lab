class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task added: \"{task}\"")

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"Task removed: \"{task}\"")
        else:
            print(f"Task not found: \"{task}\"")

    def show_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            print("To-Do List:")
            for idx, task in enumerate(self.tasks, start=1):
                print(f"{idx}. {task}")

# Example usage
todo = TodoList()
todo.add_task("Buy Food")
todo.add_task("Finish assements")
todo.show_tasks()
todo.remove_task("Buy Food")
todo.show_tasks()