FROM python:3.8

WORKDIR /app
ADD . .

RUN pip install -r requirements.txt

ENTRYPOINT ["tail", "-f", "/dev/null"]
