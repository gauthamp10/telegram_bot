FROM python:alpine3.11
RUN apk add --update --no-cache g++ gcc libxml2-dev libxslt-dev python-dev libffi-dev openssl-dev make
RUN apk add --no-cache youtube-dl
LABEL maintainer="Gautham Prakash <github.com/gauthamp10>"
COPY /src /app 
WORKDIR /app
RUN pip install -r requirements.txt
CMD python ./main.py
