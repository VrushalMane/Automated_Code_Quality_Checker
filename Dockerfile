
FROM python:3.14-slim

WORKDIR /app

# Copy dependency file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application, tests and coverage configuration
COPY app.py test_app.py .coveragerc ./

# Run code quality check
RUN python -m flake8 app.py test_app.py

# Run unit tests, generate coverage summary and HTML report
CMD ["sh", "-c", "python -m coverage run -m unittest test_app.py && python -m coverage report -m && python -m coverage html"]
