import random
import time


def unique_username(prefix: str = "qa") -> str:
    # kept short: this ParaBank instance falsely reports long usernames as
    # already taken (looks like a backend length-truncation bug), verified
    # against the live site - usernames over ~14 chars fail registration
    return f"{prefix}{str(int(time.time()))[-5:]}{random.randint(10, 99)}"


def new_user(username: str = None) -> dict:
    return {
        "first_name": "Ajay",
        "last_name": "Trainee",
        "address": "Khachhen-16",
        "city": "Patan",
        "state": "Bagmati",
        "zip_code": "44600",
        "phone": "9800000000",
        "ssn": str(random.randint(100000000, 999999999)),
        "username": username or unique_username(),
        "password": "Qa@12345",
    }


EXISTING_USERNAME = "john"  # seeded demo account on ParaBank, always present
EXISTING_PASSWORD = "demo"
