# Student Registration System – QA Testing Project

## Project Overview

This project demonstrates both **manual** and **automated UI testing** of a PHP-based Student Registration System running on a local server. The application allows users to register students by entering personal details, validating inputs, and storing records in a MySQL database.

Manual testing was performed by designing and executing test cases covering functional, validation, positive, negative, smoke, regression, UI, and database verification scenarios. Selected test scenarios were automated using Playwright with Python and Pytest.

---

## Technologies Used

- Playwright (Python)
- Pytest
- PHP
- HTML
- MySQL
- XAMPP
- Git & GitHub
- pytest-html

---

## Test Coverage

### Manual Testing

- Smoke Testing
- Functional Testing
- Positive Testing
- Negative Testing
- Validation Testing
- Boundary Value Testing
- UI Testing
- Database Verification
- Regression Testing
---
## Student_Registration_System_QA_test_documentation.xlsx
- Test case ID (TC ID)
- Module
- Test Type
- Test Case
- Preconditions
- Test Scenario
- Test Data
- Expested Result
- Actual Result
- Status
- Priority

### Automation Testing

- URL Verification
- Page Title Verification
- Form Field Visibility
- Successful Form Submission
- Empty Form Validation
- Input Field Validation
- HTML Test Report Generation

---

---

## Backend Files

### `index.php`

- Student Registration Form
- Input Validation
- Form Submission
- Data Processing

### `database.php`

- Database Connection
- Student Data Insertion into MySQL

---

## How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repository.git
```

### 2. Navigate to the Project Directory

```bash
cd Student-Registration-System-QA
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Playwright Browsers

```bash
playwright install
```

### 5. Run All Test Cases

```bash
pytest tests/
```

### 6. Generate HTML Test Report

```bash
pytest --html=reports/report.html --self-contained-html
```

### 7. Run a Specific Test File

```bash
pytest tests/test_index.py --html=reports/report.html --self-contained-html
```

---

## Test Reports

HTML execution reports are generated using **pytest-html** and are saved in the `reports/` directory.

---

## Author

**Jenisha Rai**


