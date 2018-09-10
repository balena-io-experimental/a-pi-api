FROM resin/raspberrypi3-python:3

WORKDIR /usr/src/pins

COPY ./requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt
RUN rm /requirements.txt

COPY ./src ./

ENV INITSYSTEM on

CMD [ "python", "-u", "server.py" ]
