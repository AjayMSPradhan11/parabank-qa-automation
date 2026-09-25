EXISTING_USERNAME = "john"  # seeded demo account on ParaBank, always present
EXISTING_PASSWORD = "demo"

LOGIN_CASES = [
    {
        "id": "valid_login",
        "username": EXISTING_USERNAME,
        "password": EXISTING_PASSWORD,
        "expect": "success",
    },
    {
        "id": "wrong_password",
        "username": EXISTING_USERNAME,
        "password": "wrong_password_123",
        "expect": "error",
        "expect_message": "could not be verified",
    },
    {
        "id": "nonexistent_username",
        "username": "no_such_user_qa",
        "password": "anything123",
        "expect": "error",
        "expect_message": "could not be verified",
    },
    {
        "id": "blank_username",
        "username": "",
        "password": "demo",
        "expect": "error",
        "expect_message": "VERIFY_MANUALLY",
    },
    {
        "id": "blank_password",
        "username": "john",
        "password": "",
        "expect": "error",
        "expect_message": "VERIFY_MANUALLY",
    },
]
