from models.user import User
from utils import validators
from utils import storage
from utils.helpers import hash_password

current_user = None

def login_with_email(email, password):
    global current_user
    user_data = storage.get_user_by_email(email)
    
    if not user_data:
        return False
    
    hashed_password = hash_password(password)
    if user_data["password"] != hashed_password:
        return False
    
    if user_data["status"] != "active":
        return False
    
    current_user = User.from_dict(user_data)
    return True

def register_user(user_id, fname, lname, email, mobile, password, confirm_pass):
    
   
    if not validators.is_valid_user_id(user_id):
        return False
    if storage.id_exists(user_id):
        return False
    
    if not validators.is_valid_email(email):
        return False
    if storage.email_exists(email):
        return False
    
    if not validators.is_valid_mobile(mobile):
        return False
    if storage.mobile_exists(mobile):
        return False
    
    if password != confirm_pass:
        return False
    hashed_password = hash_password(password)


    new_user = User(user_id, fname, lname, email, hashed_password, mobile)
    storage.add_user(new_user.user_to_dict())
    return True

def update_profile(fname=None, lname=None, mobile=None):
    global current_user
    if not current_user:
        return False
    
    if fname:
        current_user.fname = fname
    if lname:
        current_user.lname = lname
    if mobile:
        current_user.mobile = mobile
    
    storage.update_user(current_user.user_to_dict())
    return True

def logout():
    global current_user
    current_user = None

def get_current_user():
    return current_user

def is_admin():
    global current_user
    if not current_user:
        return False
    return current_user.role == 'admin'

def is_user():
    global current_user
    if not current_user:
        return False
    return current_user.role == 'user'

def activate_user(user_id):
    if not is_admin():
        return False
    
    return storage.activate_user(user_id)

def deactivate_user(user_id):
    current_user = get_current_user()
    if not current_user or current_user.role != "admin":
        return False
    
    return storage.deactivate_user(user_id)