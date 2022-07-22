FROM python:3.8.6

ADD requirements.txt .

RUN pip install -r requirements.txt

ADD app.py .

ADD templates ./templates/

CMD ["python", "app.py"]