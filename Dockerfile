FROM python:latest

WORKDIR /app 
COPY . /app

RUN pip install -r /app/requirements.txt

CMD [ "python3" , "bot.py"]