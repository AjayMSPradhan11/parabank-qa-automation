VALID_CONTACT = {
    "first_name": "John",
    "last_name": "Smith",
    "address": "1431 Main St",
    "city": "Beverly Hills",
    "state": "CA",
    "zip_code": "90210",
    "phone": "310-447-4121",
    "expect_heading": "Profile Updated",
}

INVALID_CONTACT = {
    "first_name": "",
    "last_name": "Smith",
    "address": "1431 Main St",
    "city": "Beverly Hills",
    "state": "CA",
    "zip_code": "90210",
    "phone": "310-447-4121",
    "expect_message": "First name is required.",
}