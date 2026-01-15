#user.py = إيه هو المستخدم؟
class User:
    def __init__(self, user_id, fname, lname, email, password, mobile, status = 'inactive', role = 'user'):
        self.id = user_id
        self.fname = fname
        self.lname = lname
        self.email = email
        self.password = password
        self.mobile = mobile
        self.status = status
        self.role = role
