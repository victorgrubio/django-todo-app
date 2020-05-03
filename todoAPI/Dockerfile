FROM python:3.6
COPY . /app
RUN apt-get install build-essential && pip install -r requirements.txt
WORKDIR /app
ENTRYPOINT ["./rebuild_project.sh"]
