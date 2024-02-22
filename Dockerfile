FROM python:3.12.1
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
#RUN apt update -y && apt install awscli -y
#EXPOSE $PORT
#CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app
CMD python app.py
#CMD gunicorn --workers=4 --bind 0.0.0.0:5000 app:app