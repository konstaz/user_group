FROM python:3.7


RUN apt-get update && apt-get install -y --no-install-recommends \
    python-dev \
    python-setuptools

WORKDIR /test_site


COPY requirements.txt /tmp/requirements.txt

RUN pip3 install -r /tmp/requirements.txt