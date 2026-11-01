
FROM python:3.14-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app.py test_app.py ./

# Run code quality check
RUN python -m flake8 app.py test_app.py

# Run automated unit tests
CMD ["python", "-m", "unittest", "-v", "test_app.py"]
