# ParaBank QA Automation Framework

Automated UI test suite for [ParaBank](https://parabank.parasoft.com/parabank/index.htm), a demo banking
web application, built with Selenium, Python and Pytest using the Page Object Model.

## Tech stack

- Python
- Selenium WebDriver
- Pytest (test runner)
- pytest-html (HTML reporting)
- pytest-rerunfailures (auto-retries a test once on failure)
- webdriver-manager (Chrome driver management)

## Project structure

```
parabank-qa-automation/
├── pages/                    # Page Object Model classes
│   ├── base_page.py          # shared wait/click/type helpers
│   ├── register_page.py
│   ├── login_page.py
│   ├── transfer_funds_page.py
│   └── bill_pay_page.py
├── tests/
│   ├── conftest.py           # driver + logged_in_driver fixtures
│   ├── test_data.py          # test data / seeded demo account
│   ├── test_register.py
│   ├── test_login.py
│   ├── test_transfer_funds.py
│   └── test_bill_pay.py
├── reports/                  # generated HTML test report
├── requirements.txt
└── pytest.ini
```

## Setup

```bash
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Requires Google Chrome installed locally. `webdriver-manager` downloads the matching
ChromeDriver automatically — no manual driver setup needed.

## Running the tests

```bash
pytest
```

This runs the full suite and generates `reports/report.html`.

Run a single file:

```bash
pytest tests/test_login.py
```

## Test case matrix

| ID | Module | Test case | Type |
|----|--------|-----------|------|
| TC01 | Registration | Register a new user successfully | Positive |
| TC02 | Registration | Register with an already-taken username | Negative |
| TC03 | Login | Log in with valid credentials | Positive |
| TC04 | Login | Log in with an invalid password | Negative |
| TC05 | Transfer Funds | Transfer an amount between accounts | Positive |
| TC06 | Bill Pay | Pay a bill with valid payee details | Positive |

## Notes

- Login/Transfer/Bill Pay tests reuse ParaBank's seeded demo account (`john` / `demo`)
  instead of registering a fresh user each run, since transfer/bill pay require an
  account with existing balances.
- Registration tests create a unique username per run (timestamp-based). This
  ParaBank instance was found (by testing directly against it) to falsely reject
  usernames longer than ~14 characters as "already exists", so generated usernames
  are kept short.
- Transfer Funds and Bill Pay pages load their account dropdowns via an async AJAX
  call after page load; `TransferFundsPage.wait_for_accounts_loaded()` waits for
  that before submitting, to avoid a race where the form submits before the
  accounts are populated.
- This is a public third-party demo site with variable latency/reliability outside
  our control. `pytest.ini` configures one automatic rerun per failing test
  (`--reruns 1`) to absorb that noise without masking genuine, repeatable failures.
