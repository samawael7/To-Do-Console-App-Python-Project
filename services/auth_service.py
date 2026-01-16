#auth_service.py = إزاي أسجل وأعمل login؟

from models.user import User
from utils import validators
from utils import storage
from utils.helpers import hash_password

def register():

    user_id = input("Enter your ID: ").strip()
    if not validators.is_valid_user_id(user_id) or storage.id_exists(user_id):
        print("failed")
        return
    
    fname = input("Enter your First Name: ").strip()

    lname = input("Enter your Last Name: ").strip()

    email = input("Enter your Email: ").strip()
    if not validators.is_valid_email(email) or storage.email_exists(email):
        print("failed")
        return
    
    mobile = input("Enter your Mobile Number: ").strip()
    if not validators.is_valid_mobile(mobile) or storage.mobile_exists(mobile):
        print("failed")
        return

    while True:
        password = input("Enter your Password: ").strip()
        confirm_pass = input("Confirm your Password: ").strip()
        if check_pass(password, confirm_pass):
            break
    
    hashed_password = hash_password(password)
    new_user = User(user_id, fname, lname, email, hashed_password, mobile)
    storage.add_user(new_user.user_to_dict())
    print("Registration successful!")


def check_pass(password, confirm_pass):
    if confirm_pass != password:
        print("Passwords do not match, try again!")
        return False
    return True