import random
import string

def generate_random_email(domain="example.com"):
    prefix = "".join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return f"{prefix}@{domain}"

def generate_random_name():
    return "User_" + "".join(random.choices(string.ascii_letters, k=5))
