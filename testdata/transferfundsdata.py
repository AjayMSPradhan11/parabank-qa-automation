TRANSFER_AMOUNT = "10"

TRANSFER_CASES = [
    {"id": "insufficient_funds", "amount": "999999", "expect": "error"},
    {"id": "zero_amount", "amount": "0", "expect": "error"},
]
