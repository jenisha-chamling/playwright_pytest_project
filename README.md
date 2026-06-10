# Student Registration System – UI Automation Testing
This project is an automated UI testing framework for a PHP-based Student Registration System running on a local server.
It is built using Playwright (Python) and Pytest to validate form functionality, UI elements, and backend responses.

Technologies Used
-Playwright (Python)
-Pytest
-HTML (Frontend)
-PHP (Backend)
-Git & GitHub
-pytest-html (for reporting)

Features / Test Coverage
-URL validation
-Page title verification
-Form field visibility check
-Positive testing (successful form submission)
-Negative testing (empty form validation)
-Input field validation
-HTML report generation

Project Structure:

tests/        -> contains Playwright test cases (test.py)
assets/       -> contains CSS file
reports/      -> HTML test reports generated after execution
venv/         -> virtual environment (not pushed to GitHub)
Backend Files:
index.php -> Contains Student Registration form UI and form validation logic
database.php -> Handles database connection and inserts form data into MySQL database

How to run
1. Clone the repository:
   git clone <your-repo-link>

2. Navigate to project directory:
   cd playwright_project

3. Install dependencies:
   pip install -r requirements.txt

4. Install Playwright browsers:
   playwright install

5. Run test cases:
   pytest tests/

6. Generate HTML report:
   pytest tests/ --html=reports/report.html --self-contained-html
