FROM ubuntu
ENV FLASK_APP=flaskr FLASK_ENV=development
WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN apt update && apt install -y python3 python3-pip libpq-dev && pip3 install -r requirements.txt 
ENTRYPOINT [ "python3" ]
CMD ["app.py"]