FROM python:3.8.5
WORKDIR /code
COPY . .
RUN pip3 install -r requirements.txt
CMD ["uvicorn", "app.main:app", "0:8000"]