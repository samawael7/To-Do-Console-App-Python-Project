#auth_service.py = إزاي أسجل وأعمل login؟

from models.user import User

def register():

    user_id = input("Enter your ID: ").strip()
    fname = input("Enter your First Name: ").strip()
    lname = input("Enter your Last Name: ").strip()
    email = input("Enter your Email: ").strip()
    mobile = int(input("Enter your Mobile Number: ").strip())
    while True:
        password = input("Enter your Password: ").strip()
        confirm_pass = input("Confirm your Password: ").strip()
        if check_pass(password, confirm_pass):
            print("Registering user...")
            break
        else:
            print("Registration failed.")
    
    return User(user_id, fname, lname, email, password, mobile)


def check_pass(password, confirm_pass):
    if confirm_pass != password:
        print(f"passwords do not match, try again!")
        return False
    return True


