FROM python:3.8.5
WORKDIR /code
COPY . .
RUN pip3 install -r requirements.txt
CMD ["uvicorn", "main:app", "--host", "127.0.0.1", "--port", "8000"]