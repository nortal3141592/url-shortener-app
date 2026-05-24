import secrets
import string

BASE62 = string.ascii_letters + string.digits

def generate_short_code(length=8) -> str:
    return ''.join(secrets.choice(BASE62) for _ in range(length))

if __name__ == "__main__":
    print(generate_short_code())