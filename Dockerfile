FROM python:3.8.5-buster
COPY . /


COPY ./requirements.txt /requirements.txt
WORKDIR /
EXPOSE 8080

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT ["gunicorn"]
CMD [ "main_server:app", "-b", "0.0.0.0:8080" ]

