# Selenium-Python-Pytest Automation Testing Project for AutomationExercise.com

This project automates the testing of [AutomationExercise.com](https://automationexercise.com) using Selenium WebDriver (Chrome only), Pytest, and Python. It covers:

- End-to-End Testing
- Data-Driven Testing
- API Testing
- Performance Testing
- Web Scraping
- Visual Testing
- Regression Testing

---

## Prerequisites: How to Prepare Your Laptop

Before you run this project, make sure your system is ready:

### 1. Install Python (Recommended: v3.9 or higher)
- Download: https://www.python.org/downloads/
- Confirm install:
```bash
python --version
```

### 2. Install Google Chrome
- Download: https://www.google.com/chrome/

### 3. Install ChromeDriver (Automatically handled)
- You do not need to install it manually.
- The project uses `webdriver-manager` to auto-download and configure the matching ChromeDriver version.

### 4. Install Git (optional)
- Download: https://git-scm.com/
- Used for cloning the repository if hosted on GitHub.

### 5. Install Virtual Environment (optional but recommended)
```bash
python -m venv venv
venv\Scripts\activate        # On Windows
source venv/bin/activate     # On Mac/Linux
```

---

## Project Setup

### 1. Clone the Project
```bash
git clone https://github.com/your-username/automationexercise-test.git
cd automationexercise-test
```

### 2. Install Required Packages
```bash
pip install -r requirements.txt
```

---

## Running the Tests

### Run all tests
```bash
pytest tests/ --html=report.html --self-contained-html
```

### Run a specific test
```bash
pytest tests/test_login.py
```

---

## Configuration
Edit `config/config.yaml` with the following contents:
```yaml
base_url: "https://automationexercise.com"
browser: "chrome"
implicit_wait: 10
```

---

## Reports

Run with HTML report:
```bash
pytest --html=report.html --self-contained-html
```

After test run, open `report.html` in your browser to view the test report.

---

## Folder Structure

- `config/` - Environment configs
- `data/` - CSV data for parameterization
- `locators/` - Element locators
- `pages/` - Page Object Model classes
- `tests/` - Test scripts
- `utils/` - Helpers and visual comparison functions

---
