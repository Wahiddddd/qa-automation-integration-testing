# QA Automation - API and Integration Testing

## Project Overview

This project is a QA Automation testing project built to practice API testing, database testing, and integration testing using Python.

The project tests a REST API built with Flask and connected to a MySQL database. Automated tests are written using pytest and Requests.

## Tech Stack

- Python
- pytest
- Requests
- Flask
- MySQL
- Git and GitHub
- GitHub Actions

## Project Structure

```text
integration-test/
├── app.py
├── conftest.py
├── requirements.txt
├── .gitignore
├── data/
│   └── test_data.py
├── db/
│   └── database.py
└── tests/
    ├── test_api_users.py
    ├── test_database.py
    ├── test_integration.py
    └── test_app.py
```

## Test Coverage

### 1. API Testing

- Create a user with valid data.
- Validate missing and empty fields.
- Validate fields with incorrect data types.
- Verify HTTP status codes and response messages.
- Test user deletion through the API.

### 2. Database Testing

- Verify the database connection.
- Retrieve users by ID.
- Insert and delete test data.
- Verify that deleted users no longer exist.

### 3. Integration Testing

- Verify that user data submitted through the API is stored correctly in MySQL.
- Compare API responses with database records.
- Use pytest fixtures for test data setup and cleanup.
- Use parametrized tests to run multiple test cases.

## How to Run the Tests

### 1. Clone the Repository

```bash
git clone https://github.com/Wahiddddd/qa-automation-integration-testing.git
cd qa-automation-integration-testing
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the Database

Configure the MySQL connection according to your local environment. Make sure the required database and tables are available before running the tests.

### 5. Run the Application

Start the Flask API using your configured Python environment:

```bash
python app.py
```

Keep the application running while executing tests that send HTTP requests to the API.

### 6. Run the Tests

Open another terminal in the project directory and run:

```bash
pytest -v
```

## Test Results

Latest local test run: **17 tests passed**.

Test results may vary depending on the database configuration and the test environment.

## Learning Objectives

This project demonstrates practical experience with:

- Writing automated API tests using pytest and Requests.
- Validating HTTP responses and response data.
- Testing database operations with MySQL.
- Using fixtures for test setup and cleanup.
- Using parametrization to test multiple scenarios.
- Organizing automated tests into separate test modules.
- Working with Git, GitHub, and a CI workflow.

## Author

Wahid Firgiyanto
