# Playwright Automation

A comprehensive test automation framework built with Playwright and pytest for web application testing.

## Project Structure

```
Playwright_Automation/
├── api/                          # API-related test utilities
├── pages/                        # Page Object Model classes
│   ├── automation_page.py       # Automation test page
│   ├── base_page.py             # Base page class with common methods
│   ├── booking_app_page.py      # Booking application page
│   ├── redtape_page.py          # Redtape application page
│   └── sauce_page.py            # Sauce Labs test page
├── tests/                        # Test files
│   ├── test_api.py              # API tests
│   ├── test_automation_web.py   # Web automation tests
│   ├── test_bookingApp.py       # Booking app tests
│   ├── test_oracle.py           # Oracle tests
│   ├── test_redtape.py          # Redtape application tests
│   └── test_sauce_login.py      # Sauce Labs login tests
├── test_data/                    # Test data files
│   ├── booking_app_data.py      # Booking app test data
│   ├── test_data.py             # General test data
│   └── test_login_data.py       # Login credentials test data
├── utils/                        # Utility modules
│   └── logger.py                # Logging utilities
├── reports/                      # Test execution reports
├── screen_shots/                # Captured screenshots
├── conftest.py                  # Pytest configuration and fixtures
├── pytest.ini                   # Pytest settings
├── requirements.txt             # Python dependencies
└── README.md                    # This file
```

## Installation

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Setup

1. Clone or navigate to the project directory:
```bash
cd Playwright_Automation
```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running Tests

### Run all tests:
```bash
pytest
```

### Run specific test file:
```bash
pytest tests/test_automation_web.py
```

### Run tests with specific marker:
```bash
pytest -m marker_name
```

### Generate HTML report:
```bash
pytest --html=reports/report.html
```

### Run with verbose output:
```bash
pytest -v
```

### Run with detailed logging:
```bash
pytest -s
```

## Project Components

### Page Object Model (pages/)
- **base_page.py**: Contains common methods and utilities for all page objects
- **automation_page.py**: Page object for automation application
- **booking_app_page.py**: Page object for booking application
- **redtape_page.py**: Page object for redtape application
- **sauce_page.py**: Page object for Sauce Labs test site

### Test Data (test_data/)
Test data files contain reusable data for test execution:
- Credentials
- Test scenarios
- Expected values
- Application-specific data

### Utilities (utils/)
Helper functions and utilities for:
- Logging and reporting
- Common operations
- Assertion helpers

## Configuration Files

- **conftest.py**: Pytest configuration with fixtures and hooks
- **pytest.ini**: Pytest settings and options
- **requirements.txt**: Python package dependencies

## Best Practices

1. Use the Page Object Model pattern for maintainability
2. Keep test data separate from test logic
3. Use descriptive test names
4. Add proper logging for debugging
5. Take screenshots on test failures
6. Keep fixtures in conftest.py for reusability

## Reporting

Test reports and screenshots are generated in:
- `reports/`: HTML and other test execution reports
- `screen_shots/`: Screenshots captured during test execution

## License

This project is part of the test automation suite.

## Support

For issues or questions about the framework, refer to the project documentation or contact the development team.
