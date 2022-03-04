FROM python:3.8-buster
WORKDIR /app
RUN apt update
RUN apt install -y gcc
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
#RUN pip3 install mood.mqueue
RUN pip3 install ipcqueue
COPY . .
ENTRYPOINT ["python3", "main.py"]

