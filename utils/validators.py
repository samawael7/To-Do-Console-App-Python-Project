from datetime import datetime
from tkinter import messagebox
import re

def is_valid_user_id(user_id):
    if len(user_id) == 14 and user_id.isdigit():
        return True
    else:
        messagebox.showerror("Error", "ID must be exactly 14 digits!")
        return False

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return True
    else:
        messagebox.showerror("Error", "Invalid email format!")
        return False

def is_valid_mobile(mobile):
    if len(str(mobile)) == 11 and str(mobile).isdigit() and str(mobile)[0] == '0' and str(mobile)[1] == '1' and str(mobile)[2] in ['0', '1', '2', '5']:
        return True
    else:
        messagebox.showerror("Error", "Invalid Egyptian mobile number!")
        return False

def is_valid_task_title(title):
    if len(title) <= 0:
        messagebox.showerror("Error", "Task title cannot be empty!")
        return False
    return True

def is_valid_priority(priority):
    valid_priority = ["low", "medium", "high"]
    if priority.lower() in valid_priority:
        return True
    else:
        messagebox.showerror("Error", "Invalid priority! Choose: Low, Medium, or High")
        return False

def is_valid_task_status(status):
    valid_status = ["to-do", "in progress", "completed"]
    if status.lower() in valid_status:
        return True
    else:
        messagebox.showerror("Error", "Invalid status! Choose: To-Do, In Progress, or Completed")
        return False

def is_valid_due_date(due_date): 
    try:
        task_due_date = datetime.strptime(due_date, "%Y-%m-%d")
        if task_due_date > datetime.now():
            return True
        else:
            messagebox.showerror("Error", "Due date must be in the future!")
            return False
    except ValueError:
        messagebox.showerror("Error", "Invalid date format! Use YYYY-MM-DD")
        return False