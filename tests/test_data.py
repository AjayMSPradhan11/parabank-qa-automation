import json
import random
import time
from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"

def unique_username(prefix: str = "qa") -> str:
    # kept short: this ParaBank instance falsely reports long usernames as
    # already taken (looks like a backend length-truncation bug), verified
    # against the live site - usernames over ~14 chars fail registration
    return f"{prefix}{str(int(time.time()))[-5:]}{random.randint(10, 99)}"


def new_user(username: str = None) -> dict:
    with open(DATA_DIR / "user_template.json") as f:
        user = json.load(f)

    user["username"] = username or unique_username()
    user["ssn"] = str(random.randint(100000000, 999999999))
    user["password"] = "Qa@12345"
    return user


EXISTING_USERNAME = "john"  # seeded demo account on ParaBank, always present
EXISTING_PASSWORD = "demo"
