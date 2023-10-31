from project.task import Task


class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        task = [task for task in self.tasks if task_name == task.name]
        if not task:
            return f"Could not find task with the name {task_name}"
        task = task[0]
        task.completed = True
        return f"Completed task {task.name}"

    def clean_section(self):
        counter = 0
        for task in self.tasks:
            if task.completed:
                self.tasks.remove(task)
                counter += 1
        return f"Cleared {counter} tasks."

    def view_section(self):
        gep = '\n'.join(task.details() for task in self.tasks)
        return f"Section {self.name}:\n{gep}"


'''test prints'''
# task = Task("Make bed", "27/05/2020")
# print(task.change_name("Go to University"))
# print(task.change_due_date("28.05.2020"))
# task.add_comment("Don't forget laptop")
# print(task.edit_comment(0, "Don't forget laptop and notebook"))
# print(task.details())
# section = Section("Daily tasks")
# print(section.add_task(task))
# second_task = Task("Make bed", "27/05/2020")
# section.add_task(second_task)
# print(section.clean_section())
# print(section.view_section())
