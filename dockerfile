FROM python:3.9.16

WORKDIR /code_email_sender

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

CMD ["python","email_sender.py"]