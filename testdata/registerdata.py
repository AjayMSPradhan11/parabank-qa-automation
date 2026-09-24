import random
import time

USER_TEMPLATE = {
    "first_name": "Ajay",
    "last_name": "Trainee",
    "address": "Khachhen-16",
    "city": "Patan",
    "state": "Bagmati",
    "zip_code": "44600",
    "phone": "9800000000",
}


def unique_username(prefix: str = "qa") -> str:
    # kept short: this ParaBank instance falsely reports long usernames as
    # already taken (looks like a backend length-truncation bug), verified
    # against the live site - usernames over ~14 chars fail registration
    return f"{prefix}{str(int(time.time()))[-5:]}{random.randint(10, 99)}"


def new_user(username: str = None) -> dict:
    user = dict(USER_TEMPLATE)

    user["username"] = username or unique_username()
    user["ssn"] = str(random.randint(100000000, 999999999))
    user["password"] = "Qa@12345"
    return user
