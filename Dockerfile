FROM python:3.8.5
WORKDIR /code
COPY . .
RUN pip3 install -r requirements.txt
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]