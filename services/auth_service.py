#auth_service.py = إزاي أسجل وأعمل login؟

from models.user import User
from utils import validators
from utils import storage
from utils.helpers import hash_password


current_user = None

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



def login():
    global current_user
    email = input("Enter your Email: ").strip()
    password = input("Enter your Password: ").strip()
    hashed_password = hash_password(password)
    user_data = storage.get_user_by_email(email)
    if user_data and user_data["password"] == hashed_password:

        if user_data["status"] != "active":
            print("Your account is inactive. Contact admin.")
            return
        
        current_user = User.from_dict(user_data)
        print(f"Login successful! Welcome {current_user.fname}")
    else:
        print("Invalid email or password.")


def update_profile():
    user = get_current_user()
    if not user:
        print("You must be logged in first!")
        return
    
    print(f"\nCurrent Profile:")
    print(f"Name: {user.fname} {user.lname}")
    print(f"Mobile: {user.mobile}")
    
    fname = input("\nEnter new first name: ").strip()
    lname = input("Enter new last name: ").strip()
    mobile = input("Enter new mobile: ").strip()
    
    if not validators.is_valid_mobile(mobile):
        return
    
    if storage.mobile_exists(mobile) and mobile != user.mobile:
        print("Mobile already exists!")
        return
    
    user.update_field(fname=fname, lname=lname, mobile=mobile)
    storage.update_user(user.user_to_dict())
    print("Profile updated successfully!")

def logout():
    global current_user
    current_user = None
    print("you have been logged out , bye byeee!")


def get_current_user():
    return current_user