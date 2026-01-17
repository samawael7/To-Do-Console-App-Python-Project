#task_service.py = إزاي أتعامل مع المهام؟
from utils import storage
from models.task import Task
from models.user import User
from services import auth_service

def create_task(title, description, priority, task_status, due_date):
    current_user = auth_service.get_current_user()
    if not current_user:
        return False
    
    new_task = Task(title, description, priority, task_status, due_date, owner_id=current_user.id)
    storage.add_task(new_task.task_to_dict())
    return True


def view_tasks():
    user = auth_service.get_current_user()
    if not user:
        return []
    if user.role == "admin":
        return storage.load_tasks()
    else:
        return storage.get_user_tasks(user.id)


def edit_task(task_title, title=None, description=None, priority=None, due_date=None, task_status=None):
    tasks = storage.load_tasks()
    for task in tasks:
        if task["owner_id"] == auth_service.get_current_user().id and task["title"] == task_title:
            if title:
                task["title"] = title
            if description:
                task["description"] = description
            if priority:
                task["priority"] = priority
            if due_date:
                task["due_date"] = due_date
            if task_status:
                task["task_status"] = task_status
            storage.save_tasks(tasks)
            return True
    return False


def delete_task(task_title): #delete tasks by user
    current_user = auth_service.get_current_user()
    if not current_user:
        return False
    
    tasks = storage.load_tasks()
    for task in tasks:
        if task["owner_id"] == auth_service.get_current_user().id or current_user.role == 'admin':
            if task["title"] == task_title:
                tasks.remove(task)
                storage.save_tasks(tasks)
                return True
    return False


def search_tasks(keyword):
    tasks = storage.load_tasks()
    result = []
    for task in tasks:
        if (task["owner_id"] == auth_service.get_current_user().id or auth_service.get_current_user().role == 'admin') and (keyword.lower() in task["title"].lower() or keyword.lower() in task["description"].lower()):
            result.append(task)
    return result
    

def sort_tasks(sort_by):  # sort_by = "due_date" أو "priority" أو "status"
    tasks = storage.load_tasks()
    user = auth_service.get_current_user()
    user_tasks = [task for task in tasks if task["owner_id"] == user.id or user.role == 'admin']
    
    if sort_by == "due_date":
        user_tasks.sort(key=lambda x: x["due_date"])
    elif sort_by == "priority":
        priority_order = {"High": 1, "Medium": 2, "Low": 3}
        user_tasks.sort(key=lambda x: priority_order.get(x["priority"], 4))
    elif sort_by == "status":
        status_order = {"Pending": 1, "In Progress": 2, "Completed": 3}
        user_tasks.sort(key=lambda x: status_order.get(x["task_status"], 4))
    
    return user_tasks
    

def filter_tasks(filter_by, filter_value):  # filter_by = "priority", filter_value = "High"
    tasks = storage.load_tasks()
    user = auth_service.get_current_user()
    filtered_tasks = [task for task in tasks if (task["owner_id"] == user.id or user.role == 'admin') and task[filter_by] == filter_value]
    return filtered_tasks
    