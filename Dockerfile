FROM python:3.10.5
RUN  apt-get -y upgrade
RUN pip install -- pip


COPY ./requirements.txt .
RUN pip install -r requirements.txt


COPY ./boom /app

WORKDIR /app

COPY ./entrypoint.sh /
ENTRYPOINT ["sh","/entrypoint.sh"]