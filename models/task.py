#task.py = what's a task?
class Task:
    def __init__(self, title, description, priority, task_status, due_date, owner_id):
        self.title = title
        self.description = description
        self.priority = priority
        self.task_status = task_status
        self.due_date = due_date
        self.owner_id = owner_id

    def task_to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "priority": self.priority,
            "task_status": self.task_status,
            "due_date": self.due_date,
            "owner_id": self.owner_id
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            data["title"],
            data["description"],
            data["priority"],
            data["task_status"],
            data["due_date"],
            data["owner_id"]
        )