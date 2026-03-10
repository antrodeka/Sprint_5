import random
import string


def generate_login():
    characters = string.ascii_lowercase + string.digits
    username = ''.join(random.choice(characters) for _ in range(6))
    return f"{username}@ya.ru"
