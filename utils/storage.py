import json
import os

USERS_FILE = os.path.join("data", "users.json")

def load_users():
    if not os.path.exists(USERS_FILE):
        return []

    with open(USERS_FILE, "r") as file:
        return json.load(file)

def save_users(users):
    with open(USERS_FILE, "w") as file:
        json.dump(users, file, indent=4)

def email_exists(email):
    users = load_users()
    return any(user["email"] == email for user in users)

def add_user(user_dict):
    try:
        users = load_users()  
        users.append(user_dict) 
        save_users(users) 
        return True 
    except Exception as e:
        print(f"Error saving user: {e}")  
        return False  
    

def id_exists(user_id):
    users = load_users()
    return any(user["id"] == user_id for user in users)
    

def mobile_exists(mobile):
    users = load_users()
    return any(user["mobile"] == mobile for user in users)

def get_user_by_email(email):
    users = load_users()
    for user in users:
        if user["email"] == email:
            return user
    return None


def update_user(updated_user_dict):
    users = load_users()
    for i, user in enumerate(users):
        if user["id"] == updated_user_dict["id"]:
            users[i] = updated_user_dict
            save_users(users)
            return True
    return False