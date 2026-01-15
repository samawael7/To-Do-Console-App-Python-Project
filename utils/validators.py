import re

def validate_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

def validate_password(password):
    return len(password) >= 6

def validate_mobile(mobile):
    return mobile.isdigit() and len(mobile) >= 10

def passwords_match(p1, p2):
    return p1 == p2
