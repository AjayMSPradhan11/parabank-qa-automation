from pages.bill_pay_page import BillPayPage


def test_pay_bill_success(logged_in_driver):
    bill_pay_page = BillPayPage(logged_in_driver)
    bill_pay_page.open()

    bill_pay_page.pay_bill({
        "name": "Electric Company",
        "address": "Khachhen-16",
        "city": "Patan",
        "state": "Bagmati",
        "zip_code": "44600",
        "phone": "9800000000",
        "account_number": "12345",
        "amount": "25",
    })

    assert "Bill Payment Complete" in bill_pay_page.text_of(bill_pay_page.confirmation_title)
