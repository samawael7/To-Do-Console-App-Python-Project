import re

def is_valid_user_id(user_id):
    if len(user_id) == 14 and user_id.isdigit():
        return True
    else:
        print("ID must be exactly 14 characters long.")
        return False
    

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return True
    else:
        print("Invalid email format")
        return False
    

def is_valid_mobile(mobile):
        if len(str(mobile)) == 11 and str(mobile).isdigit() and str(mobile)[0] == '0' and str(mobile)[1] == '1' and str(mobile)[2] in ['0', '1', '2', '5']:
            return True
        else:
             print("Invalid mobile number format")
             return False
    

