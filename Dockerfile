
FROM python:3.14-slim

WORKDIR /app

COPY app.py test_app.py ./

CMD ["python", "-m", "unittest", "-v", "test_app.py"]
