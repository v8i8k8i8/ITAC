

# ITAC Arena Automation


## Tech Stack

- Python 3.11
- Pytest
- Playwright
- Pytest-Playwright
- Pytest-HTML
- GitHub Actions

## Automated Scenarios
Current automated coverage includes:

- Valid user login
- Navigation to the Admin area
- Event creation
- Validation of created event

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd <repository-name>
```

Create and activate a virtual environment:

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Install Playwright Chromium:

```bash
playwright install chromium
```

## Running the Tests

Run all tests:

```bash
pytest
```


# Final notes
 Change the event details each time you run the test in order to create a valid event.
 The qa env is uploaded intentionally so that you can test as is.