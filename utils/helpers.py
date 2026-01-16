import hashlib

def hash_password(password):
    hashed = hashlib.sha256(password.encode()).hexdigest()
    return hashed