# Selenium + PyTest Automation Framework

Sample UI automation framework for a demo e‑commerce web app.

## Tech Stack
- Python, Selenium WebDriver
- PyTest, Allure/HTML reports
- Page Object Model (POM)
- GitHub Actions / Jenkins ready

## Features
- Page Object Model for maintainable tests
- Fixtures for browser and test data
- Markers for smoke / regression suites
- Screenshot capture on failure

## How to Run

```bash
git clone https://github.com/akhi1212/selenium-pytest-automation-framework.git
cd selenium-pytest-automation-framework
pip install -r requirements.txt
pytest -m smoke --html=report.html
