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

        
    def user_to_dict(self):
        return {
            "id": self.id,
            "fname": self.fname,
            "lname": self.lname,
            "email": self.email,
            "password": self.password,
            "mobile": self.mobile,
            "status": self.status,
            "role": self.role
            }
    
    @staticmethod
    def update_field(self, fname = None, lname = None, mobile = None):
        if fname:
            self.fname = fname
        if lname:
            self.lname = lname
        if mobile:
            self.mobile = mobile
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            data["id"],
            data["fname"],
            data["lname"],
            data["email"],
            data["password"],
            data["mobile"],
            data["status"],
            data["role"]
        )